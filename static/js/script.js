var adultCost = parseInt(document.getElementById("adult-price").innerHTML);
var childCost = parseInt(document.getElementById("child-price").innerHTML);
console.log(adultCost);
console.log(childCost);

if (document.getElementById("a-meat").innerHTML === "None") {
    var adultMeat = 0;
} else {
    var adultMeat = parseInt(document.getElementById("a-meat").innerHTML);
}

if (document.getElementById("a-veg").innerHTML === "None") {
    var adultVeg = 0;
} else {
    var adultVeg = parseInt(document.getElementById("a-veg").innerHTML);
}

if (document.getElementById("c-total").innerHTML === "None") {
    var childMeal = 0;
} else {
    var childMeal = parseInt(document.getElementById("c-total").innerHTML);
}

console.log(adultMeat);
console.log(adultVeg);
console.log(childMeal);
totalCost = (adultMeat + adultVeg) * adultCost + childMeal * childCost;

document.getElementById("total-cost").innerHTML = totalCost;

