# APS_LOGComp

## EBNF
```
<programa> ::= {<declaração>}* ;
<declaração> ::= <decl-var> | <estrutura-controle> | <decl-imprimir> | <decl-entrada> | <atribuição> | <comentário> ;
<decl-var> ::= "var" <identificador> (":" "inteiro" | ":" "texto") ["=" <expressão>] ";" ;
<decl-imprimir> ::= "imprimir" <expressão> ";" ;
<decl-entrada> ::= "entrada" <identificador> ";" ;
<atribuição> ::= <identificador> "=" <expressão> ";" ;
<comentário> ::= "//" {<caractere>}* "\n" ;
<estrutura-controle> ::= <se> | <para> ;
<se> ::= "se" "(" <expressão> ")" <declaração> ["senão" <declaração>] ;
<para> ::= "para" <atribuição> ";" <expressão> ";" <atribuição> <declaração> ;
<expressão> ::= <expressão-bin> | <identificador> | <literal> ;
<expressão-bin> ::= <expressão> <operador> <expressão> ;
<operador> ::= "+" | "-" | "*" | "/" | "." | "==" | ">" | "<" | "||" | "&&" ;
<tipo> ::= "inteiro" | "texto" ;
<identificador> ::= <letra> {<letra> | <dígito> | "_"}* ;
<literal> ::= <literal-numérico> | <literal-texto> ;
<literal-numérico> ::= <dígito> {<dígito>}* ;
<literal-texto> ::= '"' {<caractere>}* '"' ;

```
