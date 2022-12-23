const input = document.getElementById("input");
const uploadBtn = document.getElementById("upload-button");

uploadBtn.addEventListener("click", function() {
    input.click();
});

input.addEventListener("change", (event) => {
    let image_file = event.target.files[0];
    let reader = new FileReader();
    const resize_width = 400;

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
            let canvas = document.createElement("canvas");
            let ratio = resize_width / e.target.width;

            canvas.width = resize_width;
            canvas.height =  e.target.height * ratio;

            const ctx = canvas.getContext("2d");

            ctx.drawImage(image, 0, 0, canvas.width, canvas.height);

            let new_image_url = ctx.canvas.toDataURL("image/jpeg", 90);

            // display the uploaded image
            let new_image = document.createElement("img");
            new_image.src = new_image_url;
            document.getElementById("display-image").appendChild(new_image);
        }
    }
})