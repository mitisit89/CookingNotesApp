
document.querySelector('.header_burger').onclick=function(event){
    document.querySelector('.header_burger').classList.toggle ('active'),
    document.querySelector('.header_menu').classList.toggle ('active'),
    document.querySelector('body').classList.toggle ('lock');
};
