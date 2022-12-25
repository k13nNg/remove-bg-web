const input = document.getElementById("input");
const uploadBtn = document.getElementById("upload-button");
const chooseAnotherBtn = document.getElementById("chooseAnother-button");
const convertBtn = document.getElementById("convert-button");
let input_file = "";

function resize_image(event, image_to_resize, resize_width){
    let canvas = document.createElement("canvas");
    let ratio = resize_width / event.target.width;

    canvas.width = resize_width;
    canvas.height =  event.target.height * ratio;

    const ctx = canvas.getContext("2d");

    ctx.drawImage(image_to_resize, 0, 0, canvas.width, canvas.height);

    let new_image_url = ctx.canvas.toDataURL("image/jpeg", 90);

    // display the uploaded image
    let new_image = document.createElement("img");
    new_image.src = new_image_url;
    document.getElementById("display-image").appendChild(new_image);
}

chooseAnotherBtn.addEventListener("click", function() {
    input.click();
})

uploadBtn.addEventListener("click", function() {
    input.click();
});

convertBtn.addEventListener("click", function(){
    // console.log(input_file[0]);
    removeBackground(input_file[0]);
})

input.addEventListener("change", (event) => {
    let image_file = event.target.files[0];

    let reader = new FileReader();
    const resize_width = 400;

    // Grab the input file
    input_file = input.files;

    reader.readAsDataURL(image_file);

    // if there is already an image displayed, remove that image
    if(document.getElementById("display-image").firstChild){
        document.getElementById("display-image").innerHTML="";
    }
    
    reader.onload = (event) => {
        let image_url = event.target.result;

        let image = document.createElement("img");
        image.src = image_url;

        image.onload = (e) => {
            resize_image(e, image, resize_width);
            
            // change the buttons
            document.getElementById("upload-button").style.display = "none";
            document.getElementById("btn-container").style.display = "inline";
        }
    }
})