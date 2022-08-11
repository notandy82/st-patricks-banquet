var adultCost = parseInt(document.getElementById("adult-price").innerHTML);
var childCost = parseInt(document.getElementById("child-price").innerHTML);
console.log(adultCost);
console.log(childCost);
var adultMeat = parseInt(document.getElementById("a-meat").innerHTML);
var adultVeg = parseInt(document.getElementById("a-veg").innerHTML);
var childMeal = parseInt(document.getElementById("c-total").innerHTML);
console.log(adultMeat);
console.log(adultVeg);
console.log(childMeal);
adultTotal = (adultMeat + adultVeg) * adultCost;
childTotal = childCost * childMeal;
console.log(adultTotal);
console.log(childTotal);
totalCost = childTotal + adultTotal;
console.log(totalCost);

document.getElementById("total-cost").innerHTML = totalCost;
