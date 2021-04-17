/***********************************************/ 
/* Lista Encadeada                             */
/* objetivo: cadastro de pessoas               */
/* programador: Daniela Bagatini               */
/* criado em: 01/04/2016                       */
/* data da ultima alteracao: 29/09/2020        */
/***********************************************/ 


#include <stdio.h>         // entrada e sa?da padr?o: printf, scanf
#include <stdlib.h>		   // exit, malloc, system
#include <string.h>	  	   // strcmp
#include <locale.h>        // setlocale
//#include <ctype.h>       // toupper
//#include <conio.h>       // getch
//#include <time.h>        // rand   


// bibliotecas inclu?das, manter bibliotecas na mesma pasta do arquivo fonte
#include "MODELOENC.h"     // modelo de dados
#include "GERA_DADOSENC.h" // gera dados para povoar lista de forma autom?tica 

#define True 1             // constante True vale 1 


/***********************************************/ 
/* Defini??o das Fun??es                       */
/***********************************************/ 
void  entrada_dados  ( NODO *aux );           // l? dados de entrada
void  imprime_lista  ( NODO *aux );           // visualiza lista em tela
void  cria_lista     ( NODO **l );            // inicializa lista com NULL
void  destroi_lista  ( NODO **l );            // apaga lista e libera mem?ria
void  inclui_fim     ( NODO **l );            // inclui novo registro no final da lista
void  inclui_inicio  ( NODO **l );            // inclui novo registro no in?cio da lista
NODO* procura_nodo   ( NODO *l, int cod );    // procura na lista por uma c?digo
void  exclui_nodo    ( NODO **l );            // exclui regitro por c?digo 
void  ordena_lista   ( NODO **l );            // ordena lista por c?digo
void  inclui_ordenado( NODO **l );            // inclui registro na lista ordenado por c?digo
void  inverte        ( NODO **l );            // inverte refer?ncia dos registros
void  consulta_nome  ( NODO *l );             // consulta por nome
void  inserir_antes  ( NODO **l );            // insere registro antes de uma c?digo de refer?ncia
void  inserir_depois ( NODO **l );            // insere registro depois de uma c?digo de refer?ncia
void  conta_nodo     ( NODO **l );            // conta n?mero de registros existentes na lista
// crie sua pr?pria fun??o aqui!


/***********************************************/ 
/* Programa Principal                          */
/***********************************************/ 
int main( void ){
    int op;                                   // op??o do menu                               
    NODO* l;                                  // declara??o da lista - ponteiro
    setlocale(LC_ALL, "Portuguese");	      // alterar idioma para portugu?s
    
    while( True ){
         printf( "\n /----------------------------------------------------/" );  // menu
         printf( "\n Programa registro - Menu                              " );
         printf( "\n [1 ]  Cria lista                                      " );
         printf( "\n [2 ]  Inclui registro no final da lista               " );
         printf( "\n [3 ]  Inclui registro no início da lista              " );
         printf( "\n [4 ]  Exclui registro                                 " );
         printf( "\n [5 ]  Ordena lista                                    " );
         printf( "\n [6 ]  Inlcui ordenado                                 " );
         printf( "\n [7 ]  Inverte lista                                   " );         
         printf( "\n [8 ]  Consulta nome                                   " );         
         printf( "\n [9 ]  Inserir antes                                   " );           
         printf( "\n [10]  Inserir depois                                  " );     
         printf( "\n [11]  Conta registros                                 " );           
         printf( "\n [12]  Crie sua própria função aqui!                   " ); 
         printf( "\n [13]  Gera dados                                      " );  
         printf( "\n [14]  Destroi lista                                   " );
         printf( "\n [15]  Imprime lista                                   " );
		 printf( "\n [0 ]  Para sair do programa                           " );
         printf( "\n /----------------------------------------------------/" );      
         printf( "\n Opção: " );
         fflush( stdin );
         scanf("%d", &op); // tecla de op??o do menu
         
         switch( op ) {
            case 1: // rotina cria lista       
                    cria_lista( &l );
                    break;
                                
            case 2:  // rotina inclui registro no final da lista
                    inclui_fim( &l );   
                    break;
          
            case 3:  // rotina inclui registro no in?cio da lista
                    inclui_inicio( &l );
                    break;
                
            case 4:  // rotina exclui registro da lista
                    exclui_nodo( &l );
                    break;
                  
            case 5:  // rotina ordena lista
                    ordena_lista( &l );
                    break;

            case 6:  // rotina inclui ordenado
                    inclui_ordenado( &l );
                    break;
                                                                                   
            case 7: // rotina inverte lista                 
                    inverte( &l ); 
                    break;                                
                    
            case 8: // rotina consultar por um nome                 
                    consulta_nome( l ); 
                    break;             

            case 9: // rotina inserir antes de um c?digo                 
                    inserir_antes( &l ); 
                    break; 

            case 10: // rotina inserir depois de um c?digo                 
                    inserir_depois( &l ); 
                    break; 
                                                                               
            case 11: // rotina contar o n?mero de registros na lista                 
                    conta_nodo( &l ); 
                    break; 

            case 12:                  
                    // crie sua pr?pria fun??o aqui! 
                    break;
                    
            case 13: // rotina gera dados de forma autom?tica para povoar a lista
                    gera_dados( &l );
                    break;                    

            case 14: // rotina destroi lista                 
                    destroi_lista( &l );     
                    break;    

            case 15: // rotina imprime lista                 
                    imprime_lista( l );     
                    break;
										                    
            case 0: // t?rmino do programa                                          
                    exit( True ); 
                    break;
                
            default : 
                    printf( "\n Digite uma opção!" ); // n?o foi digitado uma op??o v?lida
                    break;
         } // fim switch( op )

        printf("\n");
        getchar();       // parada da tela
        //system( "cls" ); // limpar tela
     } // fim do while( 1 )
 return 0;     
} // fim do programa principal



/************************************************ 
 * entrada_dados                                *
 * objetivo: rotina para ler dados              *
 * entrada : nodo (ponteiro para o novo espaco) *
 * saida   : nodo com dados                     *
 ************************************************/
void entrada_dados( NODO *aux ){
      
    printf( "\n\n Digite a código: " ); 
    fflush( stdin );                         // limpa buffer do teclado, funciona junto com entrada de dados
    scanf("%d", &aux->info.codigo);

    printf( "\n Digite o nome: " );
    fflush( stdin );     
    gets( aux->info.nome );
  
    aux->prox = NULL;                        // n?o aponta
}



/*************************************************
 * imprime_lista                                 *
 * objetivo: rotina para imprimir dados          *
 * entrada : lista                               *
 * saida   : nenhuma                             *
 *************************************************/     
void imprime_lista( NODO *aux ){
     
    int i= 1;                       // indica n?mero de registro na lista
	 
    if( aux == NULL )               // verifica se lista vazia
        printf( "\n Lista vazia!" );
	else{
		printf( "\n O endereço (&l) onde a variável lista está na memória é: [%#p]", &aux ); 
		printf( "\n A variável lista (l) aponta para o endereço............: [%#p]", aux ); 
	    printf( "\n\n\n\n Relatório Geral ----------------------------------------- " );
        while( aux != NULL ){       // ponteiro auxiliar para percorrer a lista
               printf( "\n\n Registro[%d] \t End: [%#p] \t Prox: [%#p]", i, aux, aux->prox );               
               printf( "\n\t\t Código: %d", aux->info.codigo );
			   printf( "\t\t Nome.: %s", aux->info.nome );
               aux = aux->prox;     // aponta para o pr?ximo registro da lista
               i++;
		 } // fim while( aux != NULL )
	} // fim if( aux == NULL )
	getchar();                      // parada da tela
}



/************************************************
 * cria_lista                                   *
 * objetivo: rotina para inicializar a lista    *
 * entrada : lista                              *
 * sa?da   : NULL (inicializa lista)            *
 ************************************************/ 
void cria_lista( NODO **l ){
     
    *l = NULL;                                        // lista criada, in?cio n?o aponta
    printf( "\n Lista criada! " );
}



/************************************************ 
 * inclui_fim                                   *
 * objetivo: rotina para inserir no fim da lista*
 * entrada : lista                              *
 * saida   : lista com novo registro            *
 ************************************************/ 
void inclui_fim( NODO **l ){

    NODO *no = (NODO*) malloc (sizeof(NODO));
    if(no != NULL) {
    	entrada_dados(no);
    	if (*l == NULL)
    		*l = no;
    	else {
	    	NODO *aux = *l;
	    	while (aux->prox != NULL) {
	    		aux = aux->prox;
			}
			aux->prox = no;
			printf( "\n Registro incluido!" );
		}
	}
	else
		printf("\n Lista cheia!");
}



/*************************************************** 
 * inclui_inicio                                   *
 * objetivo: rotina para inserir no inicio da lista*
 * entrada : referencia de lista                   *
 * sa?da   : referencia lista com novo registro    *
 ***************************************************/ 
void inclui_inicio( NODO **l ){
	
    NODO *no =  ( NODO * ) malloc ( sizeof( NODO ) ); // aloca novo espaco em mem?ria
    if( no != NULL ){                                 // verifica se conseguiu alocar mem?ria para o novo registro
        entrada_dados( no );                     // l? dados
        no->prox = *l;                           // novo aponta para o primeiro existente ou para Null
        *l = no;                                 // in?cio aponta para o novo registro
        printf( "\n Registro incluido!" );
    } // fim if( no != NULL )
    else
    printf( "\n Lista cheia!" );
}




/************************************************ 
 * procura_nodo                                 *
 * objetivo: achar um registro por c?digo       *
 * entrada : lista e c?digo a ser procurado     *
 * sa?da   : posi??o ou NULL (n?o encontrou)    *
 ************************************************/ 
NODO* procura_nodo( NODO *aux, int cod ){
           
    while( aux != NULL )                                   // anda pela lista at? o final ou at? encontrar c?digo desejado
    {
      if( aux->info.codigo == cod ) return (aux);
          aux = aux->prox;                           // passa para o pr?ximo   
    }         
    return (NULL); // nodo de refer?ncia
}



/*************************************************** 
 * exclui_nodo                                     *
 * objetivo: rotina para excluir nodo da lista     *
 * entrada : lista                                 *
 * saida   : lista                                 *
 ***************************************************/ 
void exclui_nodo( NODO **l ) {
	int cod;
	NODO *excluir, *aux;

	printf("\n\n Digite a código: " ); 
    fflush( stdin );
    scanf("%d", &cod);
    if (*l == NULL) 
    	printf("Lista vazia");
	else {
		if (procura_nodo(*l, cod) == NULL)
	    	printf("Código não encontrado");
	    else {
	    	excluir = procura_nodo(*l, cod);
	    	aux = *l;
	    	if (aux == excluir)
	    		*l = excluir->prox;
			else {
				while(aux->prox != excluir)
						aux = aux->prox;
					aux->prox = excluir->prox;
			}
			free (excluir);
			printf("\n Registro excluido");
		}
	}
}


/*************************************************** 
 * ordena_lista                                    *
 * objetivo: rotina para ordenar a lista           *
 * entrada : lista                                 *
 * saida   : lista ordenada por codigo             *
 ***************************************************/ 
void ordena_lista( NODO **l ){
	
	if (*l == NULL)
		printf("Lista Vazia");
	else {
		if((*l)->prox == NULL)
			printf("Lista com 1 elemento");
		else {
			NODO *aux = *l;
			NODO *verifica = aux->prox;
			INFORMACAO guarda;	
					
			while (aux->prox != NULL) {
				while (verifica != NULL) {
					if (aux->info.codigo > verifica->info.codigo) {
						guarda = aux->info;
						aux->info = verifica->info;
						verifica->info = guarda;
					}
					verifica = verifica->prox;
				}
				aux = aux->prox;
				verifica = aux->prox;
			}
		}
	}
}



/*************************************************** 
 * inclui_ordenado                                 *
 * objetivo: rotina para inserir em ordem de codigo*
 * entrada : lista                                 *
 * saida   : lista com novo registro               *
 ***************************************************/ 
void inclui_ordenado( NODO** l ){
     

}



/*************************************************** 
 * inverte referencia                              *
 * objetivo: rotina para inverter referencia do reg*
 * entrada : lista                                 *
 * saida   : lista com referencia invertida        *
 ***************************************************/ 
void inverte( NODO** l ){
     

}



/*************************************************** 
 * consulta nome                                   *
 * objetivo: rotina para consultar                 *
 * entrada : lista                                 *
 * saida   : lista                                 *
 ***************************************************/ 
void consulta_nome( NODO* l ){
     

}



/*************************************************** 
 * inserir antes                                   *
 * objetivo: rotina para inserir antes de uma matr *
 * entrada : lista                                 *
 * saida   : lista com novo registro               *
 ***************************************************/ 
void inserir_antes( NODO** l ){
     

}



/*************************************************** 
 * inserir depois                                  *
 * objetivo: rotina para inserir antes de uma matr *
 * entrada : lista                                 *
 * saida   : lista com novo registro               *
 ***************************************************/ 
void inserir_depois( NODO** l ){
     
 
}


/*************************************************** 
 * conta_nodo                                      *
 * objetivo: rotina para contar numero de registros*
 * entrada : lista                                 *
 * saida   : nenhuma                               *
 **************************************************/ 
void conta_nodo( NODO** l ){
     

}


/*************************************************
 * destroi_lista                                 *
 * objetivo: rotina para apagar lista            *
 * entrada : lista                               *
 * saida   : lista vazia                         *
 *************************************************/ 
void destroi_lista  ( NODO **l ){
	  
    int i= 0;                      // indica n?mero de registro na lista
	 
    if( *l == NULL )               // verifica se lista vazia
        printf( "\n Lista vazia!" );
	else{
	    NODO *aux = *l;
        while( aux != NULL ){      // ponteiro auxiliar para percorrer a lista
               printf( "\n Destroi Registro[%d]", i );
               printf( "\t Código: %d", aux->info.codigo );
			   printf( "\t Nome.: %s", aux->info.nome );
			   *l = aux->prox;     // aponta para o pr?ximo registro da lista
               free( aux );        // libera mem?ria
			   aux = *l;           // reposiciona ponteiro auxiliar no in?cio      
               i++;
		 } // fim while( aux != NULL )
	} // fim if( aux == NULL )
	getchar();                     // parada da tela
}

