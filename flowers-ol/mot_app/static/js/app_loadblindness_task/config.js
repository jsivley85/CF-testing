//// parameters

//////////////////////////Monitor 
// number of pixels per degres:
let viewer_dist = 50;
/*
function get_ppd(viewer_dist, screen_params){
    return (viewer_dist*Math.tan(Math.PI/180)) * screen_params;
}
*/
let window_availw = window.screen.availWidth;
let window_availh = window.screen.availHeight;

//let window_availw = window.screen.width;
//let window_availh = window.screen.height;

let size_screen_cm_w = 34.25; // width pixels/cm in sawayama's monitor
//let screen_params = 1920/34.25; // width pixels/cm in sawayama's monitor
let screen_params = window_availw/size_screen_cm_w;
let ppd = get_ppd(viewer_dist, screen_params);
//////////////////////////Monitor 

let fname_success = 'static/images/icons/success.png';
let fname_bkg = 'static/images/pre-post-imgs/bkg_largewindow.png';
let size_bkg_width_orig = 1440; //original in pix
let size_bkg_height_orig = 1080; //original in pix
let ratio_center = 0; 
let ratio_monitor = 0.706;
Pos = new PositionManager(window_availw,window_availh);
Pos.adjust_to_bkg(size_bkg_width_orig,size_bkg_height_orig,ratio_center);
let img_bkg;

let flag_practice = true;
let flag_break = true;
let count_break = 0;
let max_break = 2;

let num_rep_main = 10; 
let num_rep_practice = 2;

let time_stimduration_main = 50; //in ms Mani et al., (2005)
let time_stimduration_practice = 1000; //in ms Mani et al., (2005)

let distance_from_center =  [Math.round(3*ppd),Math.round(6*ppd)]; //in pix;

let array_stimcond = [0,1,2,3]; //Experimental condition. 

let array_fixation = [0,1];

let time_maskduration = 1900; //in ms
let time_fixation = 1000; // in millisecond
let col_target = 255;

let col_bkg = 0;

// fixation 
let len_fixation = Math.round(0.5*ppd); // in pix
let col_fixation = 20; // in rgb
let thick_fixation = Math.round(0.1*ppd); // in pix
let length_longer = Math.round(0.2*ppd); //in pix

// text 
let col_text = 255;
let size_text = Math.round(0.7*ppd); //in pixel
let size_text_button = 24;
let Buttons = [];
////

// image
let size_img = Math.round(3.6*ppd); //in pix
let contrast_img_correct = 0.8;
let contrast_img_wrong = 0.4;
let ind_distance = [0,1];


let x_ok = -Math.round(0*ppd);
let y_ok = Math.round(4*ppd);
let x_restart = -Math.round(5.5*ppd);; //in pixel
let y_restart = -Math.round(4*ppd);; //in pixel

let x_length_answer = Math.round(3*ppd);
let y_length_answer = Math.round(4*ppd);

let x_ans1 = [Pos.center_x - len_fixation - length_longer-x_length_answer, 
    Pos.center_y+y_length_answer, 
    Pos.center_x +len_fixation + length_longer-x_length_answer, 
    Pos.center_y+y_length_answer];
let x_ans2 = [Pos.center_x - len_fixation+x_length_answer, 
    Pos.center_y+y_length_answer, 
    Pos.center_x +len_fixation+x_length_answer, 
    Pos.center_y+y_length_answer];
let y_ans1 = [Pos.center_x-x_length_answer, 
    Pos.center_y- len_fixation+y_length_answer, 
    Pos.center_x-x_length_answer, 
    Pos.center_y+len_fixation+y_length_answer];
let y_ans2 = [Pos.center_x+x_length_answer, 
    Pos.center_y- len_fixation - length_longer+y_length_answer, 
    Pos.center_x+x_length_answer, 
    Pos.center_y+len_fixation+length_longer+y_length_answer];



text_fixation_answer1 = "Horizontal";
text_fixation_answer2 = "Vertical";
size_fixation_answer_x = Math.round(4*ppd);
size_fixation_answer_y = Math.round(1.5*ppd);
x_fixation_answer1 = Pos.center_x -(size_fixation_answer_x/2)-x_length_answer;
x_fixation_answer2 = Pos.center_x -(size_fixation_answer_x/2) +x_length_answer;
y_fixation_answer = Pos.center_y -(size_fixation_answer_y/2) +Math.round(6*ppd);



let pos_guide = Math.round(1*ppd);

let text_start = "Please click the mouse to start this experiment";
let text_end = "Thank you for joining the experiment.";

let bar, success;