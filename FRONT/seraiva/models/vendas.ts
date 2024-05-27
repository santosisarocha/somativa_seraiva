import type { Livro } from "./produtos";
import type { Usuario } from "./usuario";



export type Emprestimo = {
    id?: number,
    usuarioFK: string;
    dataHora?: string;
    dataDevolucao?: string;    
} 


export type EmprestimoLivro = {
    livroFK: Livro;
    quantidade: number;
    emprestimoFK: Emprestimo;
}


export type EmprestimoLivroBody = {
    livroFK: number;
    quantidade: number;
    emprestimoFK: number;
}