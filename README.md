# APS_LOGComp

<programa> ::= {<declaração>}* ;
<declaração> ::= <decl-var> | <decl-funcao> ;
<decl-var> ::= "var" <identificador> ":" <tipo> ["=" <expressão>] ";" ;
<decl-funcao> ::= "funcao" <identificador> "(" [<lista-params>] ")" ":" <tipo> "{" {<declaração>}* "}" ;
<lista-params> ::= <param> {"," <param>}* ;
<param> ::= <identificador> ":" <tipo> ;
<expressão> ::= <identificador> | <literal> | <expressão-bin> ;
<expressão-bin> ::= <expressão> <operador> <expressão> ;
<operador> ::= "+" | "-" | "*" | "/" ;
<tipo> ::= "inteiro" | "flutuante" | "texto" | "booleano" ;
<identificador> ::= <letra> {<letra> | <dígito>}* ;
<literal> ::= <literal-numérico> | <literal-texto> | <literal-booleano> ;
<literal-numérico> ::= <dígito> {<dígito>}* ;
<literal-texto> ::= '"' {<caractere>}* '"' ;
<literal-booleano> ::= "verdadeiro" | "falso" ;
