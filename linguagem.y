%{
#include <stdio.h>
#include <stdlib.h>
extern int yylex();
extern char *yytext;
void yyerror(const char *s) { fprintf(stderr, "Erro de análise: %s\n", s); }
%}

%token VAR FUNCAO SE SENAO PARA INTEIRO FLUTUANTE TEXTO BOOLEANO VERDADEIRO FALSO
%token IDENTIFICADOR LITERAL_NUMERICO LITERAL_TEXTO LITERAL_FLUTUANTE
%token SOMA SUBTRACAO MULTIPLICACAO DIVISAO IGUAL VIRGULA ABRE_PARENTESES FECHA_PARENTESES ABRE_CHAVES FECHA_CHAVES PONTO_E_VIRGULA
%token MAIOR_QUE MENOR_QUE

%%

programa: /* vazio */
        | programa declaracao
        ;

atribuicao: IDENTIFICADOR IGUAL expressao

declaracao: decl_var
          | decl_funcao
          | estrutura_controle
          | expressao
          | atribuicao
          ;

decl_var: VAR IDENTIFICADOR tipo
        | VAR IDENTIFICADOR tipo IGUAL expressao
        ;

decl_funcao: FUNCAO IDENTIFICADOR ABRE_PARENTESES lista_params FECHA_PARENTESES ABRE_CHAVES programa FECHA_CHAVES
           ;

lista_params: /* vazio */
            | lista_params VIRGULA param
            | param
            ;

param: IDENTIFICADOR tipo
     ;

expressao: IDENTIFICADOR
         | LITERAL_NUMERICO
         | LITERAL_TEXTO
         | LITERAL_FLUTUANTE
         | VERDADEIRO
         | FALSO
         | expressao_bin
         | atribuicao

         ;

expressao_bin: expressao operador expressao
             ;

operador: SOMA
        | SUBTRACAO
        | MULTIPLICACAO
        | DIVISAO
        | MAIOR_QUE
        | MENOR_QUE
        ;

tipo: INTEIRO
    | FLUTUANTE
    | TEXTO
    | BOOLEANO
    ;

estrutura_controle: se
                  | para
                  ;

se: SE ABRE_PARENTESES expressao FECHA_PARENTESES ABRE_CHAVES programa FECHA_CHAVES
  | SE ABRE_PARENTESES expressao FECHA_PARENTESES ABRE_CHAVES programa FECHA_CHAVES SENAO ABRE_CHAVES programa FECHA_CHAVES
  ;

para: PARA atribuicao PONTO_E_VIRGULA expressao PONTO_E_VIRGULA atribuicao ABRE_CHAVES programa FECHA_CHAVES;
    ;

%%

int main() {
    if (yyparse()) {
        fprintf(stderr, "Análise falhou\n");
        return 1;
    }
    return 0;
}
