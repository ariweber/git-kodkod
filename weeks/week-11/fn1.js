
// ### תרגיל 1

// כתוב פונקציה שמקבלת שם ומחזירה הודעת שלום. 

function nameHllo(name) {
  return (`Hlooh ${name}`)
}

console.log(nameHllo("run"))

function sum(a, b) {
  return a +b
}


//     ### תרגיל 3

//     כתוב פונקציה שמחזירה `true` אם מספר זוגי, אחרת `false`.
function checkEven(a) {
  return a % 2 == 0
}

console.log(checkEven(2))
//     ---

//     ### תרגיל 4

//     כתוב פונקציה שמקבלת מערך ומחזירה את האיבר הראשון.

//     ---

function firstVal(arr) {
  return arr[0]
}
console.log(firstVal([1,2,3,4]))
//     ### תרגיל 5

//     כתוב פונקציה שמקבלת מחרוזת ומחזירה אותה באותיות גדולות.
function upperStr(str) {
  return str.toUpperCase();
}




//     מה יודפס בקוד הבא? הסבר למה.


// let x = 5;

// function test() {
//   let x = 10;
//   console.log(x);
// }

// test();
// console.log(x);



//     ### תרגיל 7

//     מה הבעיה בקוד הבא? תקן אותו.


// function test() {
//   y = 10;
//   console.log(y)
// }

// test();




//     ### תרגיל 8

//     מה יודפס?

// function a() {
//   console.log(x);
// }

// function b() {
//   let x = 2;
//   a();
// }

// b();
// שגיאה כי כדי שa ידפיס את x הוא צריך ךקבל אותו כארוגמנט


//     ### תרגיל 9

//     כתוב פונקציה שמנסה לגשת למשתנה פנימי מחוץ לפונקציה — וגרום לשגיאה.
// let x = 10
// function a(){
//     let x = 10
//     console.log(x)
// }

// console.log(x)

//     ---

//     ### תרגיל 10


function add() {
    let count = 0;
  count++;
}




//     ## תרגילים בינוניים

//     ---

//     ### תרגיל 11

//     כתוב פונקציה שמקבלת מערך מספרים ומחזירה סכום — **בלי להשתמש במשתנה גלובלי**.

function sumList(list){
    sum  = 0
    for (num of list){
        sum += num
    } return sum
}
console.log(sumList([1,2,34,4]))

//     ### תרגיל 12

//     כתוב פונקציה שמקבלת מספר ומחזירה את הריבוע שלו.

//     לאחר מכן כתוב פונקציה נוספת שמשתמשת בה.

function holding(n){
    return n*n  
}

console.log(holding(2))
//     ### תרגיל 13


let x = 10;

function test(x) {
  return x * 2;
}

console.log(test(5));


//     ## תרגילים מתקדמים


//     ### תרגיל 14

//     כתוב פונקציה שמקבלת מערך ומחזירה רק מספרים זוגיים — **ללא שימוש במשתנים חיצוניים**.

function even(list){
    for (n of list){
        if (n%2==0){
            console.log(n)
        }
    }
}
console.log(even([1,2,3,4,5,6]))

//     ### תרגיל 15

let total = 0;

function addToTotal(num) {
  total += num;
}

function reset() {
  total = 0;
}

addToTotal(5);
addToTotal(10);
reset();
console.log(total);
// הקוד מסוכן כי הוא תלוי במשתה גלובלי


