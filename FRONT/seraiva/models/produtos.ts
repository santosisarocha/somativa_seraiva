export type CategoriaProduto ={
    id: number;
    nome: string

}
export type UsuarioCustomizado ={
    id: number;
    telefone: number;
    endereco: string;
    cpf: number;
    email: string;
    nome?: string;
    foto?: string;
    biografia?: string;

}

export type Livro ={
   id: number; 
   titulo: string;
   preco: number;
   quantidade: number;
   categoriaFK: CategoriaProduto;
   fotos: String;
   estrelas: number;
   num_pag: number;
   formato: string;
   num_edicao: number;
   usuarioFK: UsuarioCustomizado
   ano: number;
}

