/*
	p1 
	Name: Broady Rivet
	Date: 1/8/22
	Course #: CSC 499 002
	Quarter: Fall 2022
	Project #: 1
*/
// colors and numbers vars will be used in the canvas function for creating the content for the program to read to know where each item is on the diferent arcs of the wheel
var colors = ["green", "black", "red", "black", "red",
            "black", "red", "black", "red", "black", "red", "black", "red",
            "black", "red", "black", "red", "black", "red", "green", "red", "black", "red", "black", "red", "black", "red", "black", "red", "black", "red", "black", "red", "black", "red", "black", "red", "black"];
var number = ["0", "28", "9", "26",
                    "30", "11", "7", "20",
                    "32", "17", "5", "22", "34", "15", "3", "24", "36", "13", "1", "00", "27", "10", "25", "29", "12", "8", "19", "31", "18", "6", "21", "33", "16", "4", "23", "35", "14", "2"];

var startAngle = 0;
var arc = Math.PI / 19;
var spinTimeout = null;
var answer;
var total = localStorage.getItem("money");
//var total = 1000;

// arc and spin times will be how the wheel determines what answer it lands on based off where the arcs are after spinning compared to original locations
var spinArcStart = 10;
var spinTime = 0;
var spinTimeTotal = 0;

// canvas content variable
var ctx;

function draw() {
    drawRouletteWheel();
}

// creating the roulette wheel whether that be before or after spinning is complete.
// uses canvas to draw visual
function drawRouletteWheel() {
    var canvas = document.getElementById("wheelcanvas");
    if (canvas.getContext) {
        // set the base dimensions of wheel and contents
        var outsideRadius = 240;
        var textRadius = 200;
        var insideRadius = 170;
        
        ctx = canvas.getContext("2d");
        ctx.clearRect(0,0,500,500);
        
        
        ctx.strokeStyle = "#000";
        ctx.lineWidth = 10;
        
        ctx.font = 'bold 20px Arial';
        
        for(var i = 0; i < 38; i++) {
        var angle = startAngle + i * arc;
        ctx.fillStyle = colors[i];
        
        // Canvas tutoial had most of these arc settings for a wheel of fortune game
        ctx.beginPath();
        ctx.arc(250, 250, outsideRadius, angle, angle + arc, false);
        ctx.arc(250, 250, insideRadius, angle + arc, angle, true);
        ctx.stroke();
        ctx.fill();
        
        ctx.save();
        ctx.shadowOffsetX = -1;
        ctx.shadowOffsetY = -1;
        ctx.shadowBlur    = 0;
        ctx.fillStyle = "#FFF";
        ctx.translate(250 + Math.cos(angle + arc / 2) * textRadius, 250 + Math.sin(angle + arc / 2) * textRadius);
        ctx.rotate(angle + arc / 2 + Math.PI / 2);
        var text = number[i];
        ctx.fillText(text, -ctx.measureText(text).width / 2, 0);
        ctx.restore();
        } 
        
        // makes arrow and reads what it has landed on
        ctx.fillStyle = "white";
        ctx.beginPath();
        ctx.moveTo(250 - 4, 250 - (outsideRadius + 5));
        ctx.lineTo(250 + 4, 250 - (outsideRadius + 5));
        ctx.lineTo(250 + 4, 250 - (outsideRadius - 5));
        ctx.lineTo(250 + 9, 250 - (outsideRadius - 5));
        ctx.lineTo(250 + 0, 250 - (outsideRadius - 13));
        ctx.lineTo(250 - 9, 250 - (outsideRadius - 5));
        ctx.lineTo(250 - 4, 250 - (outsideRadius - 5));
        ctx.lineTo(250 - 4, 250 - (outsideRadius + 5));
        ctx.fill();
    }
    }

// Next following functions for making the wheel spin smoothly were corrected and improved by anonymous poster on forum
// My own comments to describe them

// Spin function actually randomizes the entire wheels rotation time / amount of spins
function spin() {
    spinAngleStart = Math.random() * 10 + 10;
    spinTime = 0;
    spinTimeTotal = Math.random() * 3 + 4 * 1000;
    rotateWheel();
}

// Keeps time for wheel rotation so it stops once time is reached
function rotateWheel() {
    spinTime += 30;
    if(spinTime >= spinTimeTotal) {
        stopRotateWheel();
        return;
    }
    // starts to slow wheels rotation
    var spinAngle = spinAngleStart - easeOut(spinTime, 0, spinAngleStart, spinTimeTotal);
    // determining the new angle of the original circle that the arrow is now pointing to
    startAngle += (spinAngle * Math.PI / 180);
    drawRouletteWheel();
    spinTimeout = setTimeout('rotateWheel()', 30);
}

// function to halt the spinning of the wheel and save its current state so it doesnt reset to original orientation
function stopRotateWheel() {
    clearTimeout(spinTimeout);
    var degrees = startAngle * 180 / Math.PI + 90;
    var arcd = arc * 180 / Math.PI;
    var index = Math.floor((360 - degrees % 360) / arcd);
    ctx.save();
    ctx.font = 'bold 60px Arial';
    var text = number[index];
    answer = text;
    ctx.fillText(text, 250 - ctx.measureText(text).width / 2, 250 + 10);
    checkwin();
    ctx.restore();
}

// This function was added by poster to make the spinning not just stop abruptly.
// allows "slowing down" of the wheels rotation
function easeOut(t, b, c, d) {
    var ts = (t/=d)*t;
    var tc = ts*t;
    return b+c*(tc + -3*ts + 3*t);
}

// calling function to create the original wheel on page load
draw();

// set current money
document.getElementById("money").innerHTML = "You Have " + total + "$";

console.log(document.getElementById("2").className);
// on click function
function betfun(obj){
    // if the object that is clicked has not been clicked yet, change class to used on click
    if(obj.className == "red"){
        obj.className = "usedR";
    }
    else if(obj.className == "black"){
        obj.className = "usedB";
    }
    else if(obj.className == "zero"){
        obj.className = "usedZ";
    }
    else if(obj.className == "outterRight-tableItem"){
        obj.className = "usedOT";
    }
    else if(obj.className == "innerRight-tableItem"){
        obj.className = "usedIT";
    }
    else if(obj.className == "bottom-tableItem"){
        obj.className = "usedBT";
    }

    // become unused if clicked again
    else if(obj.className == "usedR"){
        obj.className = "red";
    }
    else if(obj.className == "usedB"){
        obj.className = "black";
    }
    else if(obj.className == "usedZ"){
        obj.className = "zero";
    }
    else if(obj.className == "usedOT"){
        obj.className = "outterRight-tableItem";
    }
    else if(obj.className == "usedIT"){
        obj.className = "innerRight-tableItem";
    }
    else if(obj.className == "usedBT"){
        obj.className = "bottom-tableItem";
    }
}
    

// can only bet 10 per square
function checkwin(){
    if ( answer != 0 && answer != 00 ){
        answer = parseInt(answer)
        // loop for any single number pick. profit = 350
        for (var i = -1 ; i <= 36 ; i++){
            newI = document.getElementById(i).className;
            if (newI == "usedR" || newI == "usedB" || newI == "usedZ"){
                if (document.getElementById(i).innerHTML == answer){
                    total -= 10;
                    total += 360;
                }
                else{
                    total -= 10;
                }
            }
        }
        // 2 to 1 column payout. profit = 20
        for (var i = 37 ; i <= 39 ; i++){
            if (document.getElementById(i).className == "usedBT"){
                if (i%3 == answer%3){
                    total -= 10;
                    total += 30;
                    }
                else
                    total -= 10;
            }
                
            }
        
        // 2 to 1 numerical payout (1-12, 13-24, 25-36). profit = 20
        for (var i = 40 ; i <= 42 ; i++){
            if (document.getElementById(i).className == "usedIT"){
                //if ((answer <= i%39*12) && (answer >= i%39*12-11)){  *math just wrong
                if(i == 40){
                    if(answer <= 12){
                        total -= 10;
                        total += 30;
                    }
                    else
                        total -= 10;
                    }
                if(i == 41){
                    if(12 < answer && answer <= 24){
                        total -= 10;
                        total += 30;
                    }
                    else
                        total -= 10;
                    }
                if(i == 42){
                    if(24 < answer && answer <= 36){
                        total -= 10;
                        total += 30;
                    }
                    else
                        total -= 10;
                }
            }
            }
        
        // Low or High half payout. profit = 10
        for (var i = 43 ; i <= 44 ; i++){
            if (document.getElementById(i).className == "usedOT"){
                if (answer <= i%42*18 && answer >= i%42*18-17){
                    total -= 10;
                    total += 20;
                }
                else
                    total -= 10;
            }
        }
        // Odd an Even payouts. proit = 10
        for (var i = 45 ; i <= 46 ; i++){
            if (document.getElementById(i).className == "usedOT"){
                if (answer%2 == i%2){
                    total -= 10;
                    total += 20;
                }
                else
                    total -= 10;
            }
        }
        // Red payout. profit = 10
        for (var i = 47 ; i <= 47 ; i++){
            if (document.getElementById(i).className == "usedOT"){
                if(answer == 1 || answer == 3 || answer == 5 || answer == 7 || answer == 9 || answer == 12 || answer == 14 || answer == 16 || answer == 18 || answer == 19 || answer == 21 || answer == 23 || answer == 25 || answer == 27 || answer == 30 || answer == 32 || answer == 34 || answer == 36){
                    total -= 10;
                    total += 20;
                }
                else
                    total -= 10;
            }				
        }
        // Black payout. profit = 10
        for (var i = 48 ; i <= 48 ; i++){
            if (document.getElementById(i).className == "usedOT"){
                if(answer == 2 || answer == 4 || answer == 6 || answer == 8 || answer == 10 || answer == 11 || answer == 13 || answer == 15 || answer == 17 || answer == 20 || answer == 22 || answer == 24 || answer == 26 || answer == 28 || answer == 29 || answer == 31 || answer == 33 || answer == 35){
                    total -= 10;
                    total += 20;
                }
                else
                    total -= 10;
            }
        }
    }
    else{
        // None winner
        for ( var i = -1; i <= 48; i++){
            newI = document.getElementById(i).className;
            if (newI == "usedR" || newI == "usedB" || newI == "usedOT" || newI == "usedIt" || newI == "usedBT"){
                total -= 10;
            }
            else if(newI == "usedZ"){
                if(document.getElementById(i) == document.getElementById("1")){
                    if(answer == 00){
                        total -= 10;
                        total += 360;
                    }
                    else
                    total -= 10;
                }
                else if (document.getElementById(i) == document.getElementById("0")){
                    if(answer == 0){
                        total -= 10;
                        total += 360;
                    }
                    else
                    total -= 10;
            }
        }
        }
    }
    document.getElementById("money").innerHTML = "You Have " + total + "$";
    localStorage.setItem("money",total);
}