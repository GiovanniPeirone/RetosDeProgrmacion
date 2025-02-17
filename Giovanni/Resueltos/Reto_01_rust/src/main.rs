
fn main() {
    println!("{}", entero_a_romano(34));
}


fn entero_a_romano(mut numero : i32) -> String{

    
   let mut numero_romano = String::new();

    let simbolos = [
        ("M", 1000),
        ("CM", 900), 
        ("D", 500), 
        ("CD", 400),
        ("C", 100), 
        ("XC", 90), 
        ("L", 50), 
        ("XL", 40),
        ("X", 10), 
        ("IX", 9), 
        ("V", 5), 
        ("IV", 4), 
        ("I", 1)
    ];
    
    for (simbolo, valor) in simbolos.iter(){
        while numero >= *valor{
            numero_romano.push_str(simbolo);
            numero -= *valor
        }

    }


    numero_romano
}
