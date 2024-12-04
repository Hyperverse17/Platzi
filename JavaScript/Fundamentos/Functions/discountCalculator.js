
function currencyFormatter({ currency, value}) {
    const formatter = new Intl.NumberFormat('en-US', {
      style: 'currency',
      minimumFractionDigits: 2,
      currency
    }) 
    return formatter.format(value)
  }
  
function calculateDiscount(originalprice,discountPercentage){
    if (discountPercentage < 100){
        const discount = (originalprice*discountPercentage)/100;
        const newprice = originalprice-discount;
        return newprice;
    } else if(discountPercentage == 100){
        return "it's Free...";
    } else{
        return "Error!";
    }
}

const numero = 3500.51;
const formateado = numero.toLocaleString("en");
console.log(formateado);

// const formateado = numero.toLocaleString("en",{style: "currency",currency: "MXN"});

let originalPrice = 1599.00;
let originalPriceFmt = originalPrice.toLocaleString("en",{style: "currency",currency: "MXN"});
let discountPercentage = 35.9;
let newprice = calculateDiscount(originalPrice,discountPercentage);
let newpriceFmt = newprice.toLocaleString("en",{style: "currency",currency: "MXN"});

console.log()
console.log(`Precio Original      : ${originalPriceFmt}`)
console.log(`Descuento            : ${discountPercentage}%`)
console.log(`Precio con descuento : ${newpriceFmt}`)
console.log()