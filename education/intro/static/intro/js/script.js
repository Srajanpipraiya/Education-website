// const bar = document.getElementById("bar");
// const close = document.getElementById("close");
// const nav = document.getElementById("navbar");
// if (bar){
//     bar.addEventListener("click",() => {
//         nav.classList.add('active');
//     })
// }

// if (close){
//     close.addEventListener("click",() => {
//         nav.classList.remove('active');
//     })
// }
// if (nav){
//     window.addEventListener("scroll",()=>{
//         nav.classList.remove("active")
//     })
// }
// Toggle Style Switcher
// const styleSwitcherToggle= document.querySelector("#bar");
// styleSwitcherToggle.addEventListener("click",()=>{
//     document.querySelector("#mobile").classList.toggle("open");
// })

// hide style Switcher on scroll
// window.addEventListener("scroll",()=>{
//     console.log("scrolled");
//     if (document.querySelector(".mob").classList.contains("active"))
//     {
//         document.querySelector(".mob").classList.remove("open");
//     }
// })

// const input = document.getElementById("input");
// const list = document.getElementById("list");

// function addItem() {
//   if (input.value.trim()) {
//     const item = document.createElement("li");
//     item.innerText = input.value.trim();
//     item.addEventListener("click", toggleItem);
//     const button = document.createElement("button");
//     button.innerText = "X";
//     button.addEventListener("click", deleteItem);
//     item.appendChild(button);
//     list.appendChild(item);
//     input.value = "";
//   }
// }

// function toggleItem() {
//   this.classList.toggle("completed");
// }

// function deleteItem() {
//   this.parentNode.remove();
// }



// Myscript.js
$('#slider1, #slider2, #slider3').owlCarousel({
  loop: true,
  margin: 20,
  responsiveClass: true,
  responsive: {
      0: {
          items: 1,
          nav: false,
          autoplay: true,
      },
      600: {
          items: 3,
          nav: true,
          autoplay: true,
      },
      1000: {
          items: 5,
          nav: true,
          loop: true,
          autoplay: true,
      }
  }
})

// Ajax, it use for page withput Refresh
$('.plus-cart').click(function(){
  var id = $(this).attr("pid").toString();
  
  var eml= this.parentNode.children[2]
  $.ajax({
      type:"GET",
      url:"/pluscart",
      data:{
          prod_id: id
      },
      success: function(data) {
          eml.innerText = data.quantity
          document.getElementById("amount").innerText=data.amount
          document.getElementById("totalamount").innerText=data.totalamount
      }
  })
})

$('.minus-cart').click(function(){
  var id = $(this).attr("pid").toString();
  var eml= this.parentNode.children[2]
  $.ajax({
      type:"GET",
      url:"/minuscart",
      data:{
          prod_id: id
      },
      success: function(data) {
          eml.innerText = data.quantity
          document.getElementById("amount").innerText=data.amount
          document.getElementById("totalamount").innerText=data.totalamount
      }
  })
})
$('.remove_cart').click(function(){
  var id = $(this).attr("pid").toString();
  var eml= this
  $.ajax({
      type:"GET",
      url:"/removecart",
      data:{
          prod_id: id
      },
      success: function(data) {
          document.getElementById("amount").innerText=data.amount
          document.getElementById("totalamount").innerText=data.totalamount
          eml.parentNode.parentNode.parentNode.parentNode.remove()
      }
  })
})
/* Set the width of the sidebar to 250px and the left margin of the page content to 250px */
function openNav() {
    document.getElementById("mySidebar").style.width = "250px";
    document.getElementById("main").style.marginLeft = "250px";
  }
  
  /* Set the width of the sidebar to 0 and the left margin of the page content to 0 */
  function closeNav() {
    document.getElementById("mySidebar").style.width = "0";
    document.getElementById("main").style.marginLeft = "0";
  }
