var img = document.getElementById('img')
var image = document.getElementById('image')

img.addEventListener('change', function(){
  const file = this.files[0]

  if (file) {
    const reader = new FileReader()
    image.style.display = "block"
    reader.addEventListener('load', function(){
      image.setAttribute('src', this.result)
    })


    reader.readAsDataURL(file)
  }
})