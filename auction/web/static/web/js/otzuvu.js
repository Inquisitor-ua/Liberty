function main(){
    const stars = document.querySelectorAll('.for-click');
    stars.forEach(star => {
        star.addEventListener('click', () => {
            // Считываем значение 'data-value' у нажатой звезды
            const rating = parseInt(star.getAttribute('data-value'), 10);
            const star_class = star.getAttribute('class').split(' ').slice(0, 2).join(' ');
            const row_stars = Array.from(document.getElementsByClassName(star_class));
            const value = parseInt(star.getAttribute('data-value'), 10);
            const type_input = star.getAttribute('class').split(' ')[1];
            const inputs = Array.from(document.getElementsByTagName('input'));
            for (let i = 0; i < inputs.length; i++) {
                if (inputs[i].getAttribute('name') == type_input){
                    inputs[i].setAttribute('value', value)
                }
            }
            // Проходимся по всем звёздам и заполняем те, чей data-value <= rating
            row_stars.forEach(s => {
                const currentValue = parseInt(s.getAttribute('data-value'), 10);
                if (currentValue <= rating) {
                    s.classList.add('filled');
                } else {
                    s.classList.remove('filled');
                }
                });

            console.log('Ваша оценка: ' + rating);
        });
    });


    const carousel = document.getElementById('carousel');
    const cardWidth = document.querySelector('.otzuv-karta').offsetWidth + 30; 

    carousel.addEventListener('wheel', (e) => {
        e.preventDefault();
        carousel.scrollLeft += e.deltaY > 0 ? cardWidth : -cardWidth;
        updateCardOpacity();
    });

    // document.querySelector('#otzuv-form').addEventListener("submit", function(event) {
    //     const mark_speed = document.querySelectorAll(".mark_speed");
    //     const mark_trak = document.querySelectorAll(".mark_trak");
    //     const mark_all = document.querySelectorAll(".mark_all");
    //     let ar = [mark_speed, mark_trak, mark_all];
    //     for(i = 0; i <= 2; i++){
    //         ar[i].forEach(star => {
    //             if(!star.classList.contains('filled')){
    //                 console.log('Не заполнена звезда');
    //                 // event.preventDefault();
    //             };
    //         });
    //     };
    // });
};

main()