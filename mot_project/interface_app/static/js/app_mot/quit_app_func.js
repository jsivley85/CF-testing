function display_exit(){
    width = 100;
    height = 45;
    push();
    button_exit.position(windowWidth-(width*1.3), 50 - (height/2));
    button_exit.size(width,height);
    button_exit.mousePressed(quit_game);

    // button_pause.position(windowWidth-(width*1.3), 80 );
    // button_pause.size(width, height);
    // button_pause.mousePressed(quit_game);
    pop();
}
function quit_game(){
        // put here current results !
        fullscreen(false);
        // Put game status in parameter_dict:
        parameter_dict['game_end'] = game_end;
        if(!game_end){
            // User left game:
            parameter_dict['game_time'] = game_time;
        }
        post('mot_close_task', parameter_dict, 'post')
}