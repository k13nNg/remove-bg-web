const real_file_reader_Btn = document.getElementById("real-file-reader");
const customBtn = document.getElementById("custom-button");
//const image_input = document.querySelector("#real-file-reader");

var uploaded_image = "";

real_file_reader_Btn.addEventListener("change", function(){
    const reader = new FileReader();
    reader.addEventListener("load", () => {
        uploaded_image = reader.result;
        const ctx = document.getElementById("display-image");
        document.querySelector("#display-image").style.backgroundImage = `url(${uploaded_image})`;
        
    });
    reader.readAsDataURL(this.files[0]);
})

customBtn.addEventListener("click", function() {
    real_file_reader_Btn.click();
});

console.log (customBtn)