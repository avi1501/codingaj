function classToggle() {
    alert("JS Function");
    const navs = document.querySelectorAll('.nav__links').style.display="block";
    
    // navs.forEach(nav => nav.classList.toggle('nav__links'));
  }
  
  document.getElementsByClassName('.menu__button').addEventListener('click', classToggle);