/*
 *
 *	ENTRY POINT
 *  WEBPACK bundle app
 *  client side
 */
import "../css/app.css";

/*
 *	Class Bundle App
 */
class App {
  constructor() {
    document.getElementById("result").innerHTML = this.diviseInteger(4,5) ;

    /*let a = 2
    let b = 3
    let result = this.addInteger(a, b);
    console.warn(`Le resultat de ${a} + ${b} est : ${result}`)
    a = "2";
    b = "5";
    let result2 = this.multipliInteger(a, b);
    console.warn(`Le resultat de ${a} * ${b} est : ${result2}`)
    a = 2;
    b = "9";
    let result3 = this.addInteger(a, b);
    console.warn(`Le resultat de ${a} + ${b} est : ${result3}`)
    a = "7";
    b = 9;
    let result4 = this.multipliInteger(a, b);
    console.warn(`Le resultat de ${a} * ${b} est : ${result4}`)
    a = 10;
    b = 0;

    let result5 = this.diviseInteger(a, b);
    console.warn(`Le resultat de ${a} / ${b} est : ${result5}`)*/
  }


  addInteger(x, y) {
    //console.log( `   valeur = ${x} type : ${typeof(x)} ` );
    if (typeof (x) === "string") {
      x = parseInt(x);
    }
    //console.log( `   valeur = ${y} type : ${typeof(y)} ` );
    if (typeof (y) === "string") {
      y = parseInt(y);
    }
    return (x + y);
  }

  multipliInteger(x, y) {
    if (typeof (x) === "string") {
      x = parseInt(x);
    }
    if (typeof (y) === "string") {
      y = parseInt(y);
    }
    return (x * y);
  }

  diviseInteger(x, y) {
    if (y === 0 ){
      let error =  "la divion par 0 est interdite" ;
      throw  error
    }
    if (typeof (x) === "string") {
      x = parseInt(x);
    }
    if (typeof (y) === "string") {
      y = parseInt(y);
    }
    return (x / y);
  }

}

/*
 * HMR
 */
if (module.hot) {
  module.hot.accept((err) => {
    if (err) {
      console.error('Cannot apply HMR update.', err);
    }
  });
}
export default new App();
