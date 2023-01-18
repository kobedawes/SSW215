document.getElementById("mainMenu").innerHTML = ['Drinks <br>', 'Foods<br>', 'Homemade Coffee<br>'].join();

document.getElementById('coffees').innerHTML = ['Veranda Blend<br>', 'Cappuccino<br>', 'Expresso<br>'].join();

document.getElementById('foodMenu').innerHTML = ["Crispy Grilled Cheese on Sourdough <br>A delicious blend of white Cheddar and mozzarella cheeses on sourdough bread, topped with a Parmesan butter spread <br><br> Chicken Caprese on Ciabatta<br> Stacked with craveable ingredients, including slow-cooked chicken, mozzarella, balsamic-marinated tomatoes, basil pesto and spinach, all nestled between soft ciabatta bread. Chickens are raised without the use of antibiotics.<br><br> Eggs and Gouda Protein Box<br> Two cage-free hard-boiled eggs paired with Gouda and multigrain crackers, plus a blend of dried apricots and apples, a peanut-butter spread, salt and pepper, make this the balanced protein-packed box good for all day enjoyment.<br>"].join();


function message() {
document.getElementById('statement').innerHTML = 'Thank you for keeping us in business with your continuous patronage, you are valued as our customer';
}

document.querySelector('h4').style.color= 'green';

function color1() {
document.body.style.backgroundColor= 'lightblue';
}

function color2() {
document.body.style.backgroundColor= 'linen';
}

document.getElementbyId('todayDate').innerHTML = 'February 6th, 2022';

