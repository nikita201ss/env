
function changeImage(src) {
    const mainImage = document.getElementById('mainImage');
    if (mainImage) {
        mainImage.src = src;
        

        document.querySelectorAll('.extra-img').forEach(img => {
            img.classList.remove('active');
            if (img.src === src) {
                img.classList.add('active');
            }
        });
    }
}


function showPhoneNumber(element) {
    const phoneNumber = element.dataset.phone;
    const phoneText = element.querySelector('.phone-text');
    
    if (phoneText.textContent === 'Увидеть номер') {

        let formattedPhone = phoneNumber;
        

        if (phoneNumber.length === 11) {
            if (phoneNumber.startsWith('8')) {
                formattedPhone = phoneNumber.replace(/(\d{1})(\d{3})(\d{3})(\d{2})(\d{2})/, '+7 ($2) $3-$4-$5');
            } else if (phoneNumber.startsWith('7')) {
                formattedPhone = phoneNumber.replace(/(\d{1})(\d{3})(\d{3})(\d{2})(\d{2})/, '+$1 ($2) $3-$4-$5');
            }
        } else if (phoneNumber.length === 10 && !phoneNumber.startsWith('8')) {
            formattedPhone = phoneNumber.replace(/(\d{3})(\d{3})(\d{2})(\d{2})/, '($1) $2-$3-$4');
        }
        
        phoneText.textContent = formattedPhone;
    }
}


document.addEventListener('DOMContentLoaded', function() {

    const mainImageSrc = document.getElementById('mainImage')?.src;
    if (mainImageSrc) {
        document.querySelectorAll('.extra-img').forEach(img => {
            if (img.src === mainImageSrc) {
                img.classList.add('active');
            }
        });
    }
    

    document.querySelectorAll('.phone-button').forEach(button => {
        button.addEventListener('click', function() {
            showPhoneNumber(this);
        });
    });
});


document.addEventListener('click', function(event) {
    const phoneButtons = document.querySelectorAll('.phone-button');
    const isClickInside = Array.from(phoneButtons).some(button => button.contains(event.target));
    
    if (!isClickInside) {
        document.querySelectorAll('.phone-button .phone-text').forEach(text => {
            if (text.textContent !== 'Увидеть номер') {
                text.textContent = 'Увидеть номер';
            }
        });
    }
});