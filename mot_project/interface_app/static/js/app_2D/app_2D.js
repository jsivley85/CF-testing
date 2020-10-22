// Variables needed for object in canvas:
let window_width;
let window_height;
let canvas;
let hover_color;
let app;
let delta = 0; // camera angle for answering phase
let back = false; // variable used by camera to get back to initial position
let answer_phase = false;
// "default parameter dict":
//let parameter_dict = {n_targets:4, n_distractors:4,
//    target_color: 'red', distractor_color:'yellow',
//    radius_min:90, radius_max:120, speed_min:4, speed_max:6,
//    episode_number:0, nb_retrieved: [0,0]
//};
let background_img;
let shark_img;
let parameter_dict = {};
let results = {};
// clear session storage:
sessionStorage.clear();

// p5.js functions to display the game:
function preload() {
  // Load model with normalise parameter set to true
    // background_img = loadImage('/static/images/starBackground.png');
    background_img = loadImage('/static/images/maxresdefault.jpg');
    shark_img = loadImage('/static/images/sha1.png')
}
function setup(){
    window_height = 0.9*windowHeight;
    window_width = 0.9*windowWidth;
    canvas = createCanvas(window_width, window_height);
    canvas.parent('app_holder');
    hover_color = color(255, 255, 255);
    hover_color.setAlpha(200);
    start_episode();
}
function draw(){
    // background(100);
    background(background_img);
    noFill();
    if(app.phase=='fixation'||app.phase == 'got_response'){app.change_to_initial_color()}
    app.display_balls(mouseX, mouseY);
    app.check_collisions();
    app.move_balls();
}
function mousePressed(event) {
   // First test if objects are in "clickable mode"
   if (app.distractors[0].hover) {
       app.check_mouse_pressed(mouseX, mouseY);
   }
}
function timer(app, fixation_time, tracking_time, answer_time){
    setTimeout(function () {
        app.phase = 'fixation';
        app.frozen = true;
        setTimeout(function(){
            app.phase = 'tracking';
            app.frozen = false;
            app.change_to_same_color();
            setTimeout(function(){
                app.phase = 'answer';
                app.frozen = true;
                app.enable_hover();
                show_answer_button();
                },answer_time)
        }, tracking_time)
    }, fixation_time);
}
function windowResized(){
      createCanvas(0.9*windowWidth, 0.9*windowHeight);
}

// Additional functions to interract with user:
function start_episode(){
    if(parameter_dict['episode_number']<8){
        app = new App(parameter_dict['n_targets'], parameter_dict['n_distractors'],
                    parameter_dict['target_color'], parameter_dict['distractor_color'],
                    window_width, window_height, parameter_dict['radius_min'], parameter_dict['radius_max'],
                    parameter_dict['speed_min'], parameter_dict['speed_max'], hover_color);
        app.change_to_same_color();
        // check whether the timer could be incorporate to app!
        timer(app, 2000, 2000, 5000);
    }else{
        quit_game();
    }
}
function show_answer_button(){
    document.getElementById("button_app").type = 'submit';
    document.getElementById("button_quit").classList.remove('offset-md-8');
}
function answer_button_clicked(){
    if(document.getElementById("button_app").value == 'Next_episode' ){
        document.getElementById("button_app").type = 'hidden';
        document.getElementById("button_app").value = 'Answer';
        document.getElementById("button_quit").classList.add('offset-md-8');
        next_episode();
    }
    else{
        results = app.get_results();
        parameter_dict['nb_target_retrieved'] = results[0];
        parameter_dict['nb_distract_retrieved'] = results[1];
        if(document.getElementById("button_app").value == 'Answer' ){
            console.log("clicked");
            app.phase = 'got_response';
            app.frozen = true;
            document.getElementById("button_app").value = 'Next_episode';
        }
    }
}
function quit_game(){
        // put here current results !
        post('home', parameter_dict, 'post')
}
function next_episode(){
    //console.log(parameter_dict);
    $.ajax({
    async: false,
    type: "POST",
    url: "/next_episode",
    dataType: "json",
    traditional: true,
    data: parameter_dict,
    success: function(data) {
        parameter_dict = data;
        }
    });
    start_episode();
}