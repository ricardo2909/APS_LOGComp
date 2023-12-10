# APS_LOGComp

## EBNF
```
<programa> ::= {<declaração>}* ;
<declaração> ::= <decl-var> | <estrutura-controle> | <decl-imprimir> | <decl-entrada> ;
<decl-var> ::= "var" <identificador> ":" <tipo> ["=" <expressão>] ";" ;
<decl-imprimir> ::= "imprimir" <expressão> ";" ;
<decl-entrada> ::= "entrada" <identificador> ";" ;
<expressão> ::= <identificador> | <literal> | <expressão-bin> ;
<expressão-bin> ::= <expressão> <operador> <expressão> ;
<operador> ::= "+" | "-" | "*" | "/" ;
<tipo> ::= "inteiro" | "texto" ;
<identificador> ::= <letra> {<letra> | <dígito>}* ;
<literal> ::= <literal-numérico> | <literal-texto> ;
<literal-numérico> ::= <dígito> {<dígito>}* ;
<literal-texto> ::= '"' {<caractere>}* '"' ;
<estrutura-controle> ::= <se> | <para> ;
<se> ::= "se" "(" <expressão> ")" <declaração> ["senão" <declaração>] ;
<para> ::= "para" "[" <expressão> "]" ";" "[" <expressão> "]" ";" "[" <expressão> "]" <declaração> ;

```
