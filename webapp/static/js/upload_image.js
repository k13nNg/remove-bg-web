const real_file_reader_Btn = document.getElementById("real-file-reader");
const customBtn = document.getElementById("custom-button");
//const image_input = document.querySelector("#real-file-reader");

var uploaded_image = "";

real_file_reader_Btn.addEventListener("change", function(){
    const reader = new FileReader();

    reader.addEventListener("load", () => {
        var img = new Image(),
        canvas = document.getElementById("display-image"),
        ctx = canvas.getContext("2d");

        img.src = reader.result;
        // document.querySelector("#display-image").style.backgroundImage = `url(${uploaded_image})`;
        

        console.log("img.width: ", this.width);
        console.log("img.height: ", this.height);
        img.onload = function(){
            let width = img.width;
            let height = img.height;

            canvas.width=width;
            canvas.height=height;
            ctx.drawImage(img, 0, 0, img.width, img.height);
        }
        
    });

    reader.readAsDataURL(this.files[0]);
    
    
})

customBtn.addEventListener("click", function() {
    real_file_reader_Btn.click();
});