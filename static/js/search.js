var button = document.getElementById('search_btn')
button.addEventListener('click',search)
document.getElementById("search_char").addEventListener("keyup",search)

function search(){
    var post = document.querySelectorAll('.post')
    var post_title = document.querySelectorAll('.post_title')
    var post_detail = document.querySelectorAll('.post_detail')
    var search_char = document.getElementById("search_char").value.toLowerCase().trim()
    if(search_char.length > 1){
        for(var i=0;i<post.length; i++){
            if(post_title[i].innerHTML.toLowerCase().includes(search_char) || post_detail[i].innerHTML.toLowerCase().includes(search_char)){
                post[i].style.display = "block"
                // console.log(post[i])
            }else{
                post[i].style.display = "none"
            }
        }
    }else if(search_char.length == 0){
        pagination(ID)
    }
}