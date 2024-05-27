import { BACKEND_URL } from "~/models/app";
import type { Emprestimo, EmprestimoLivro, EmprestimoLivroBody } from "~/models/vendas";

export const salvarVenda = (venda: Emprestimo): Promise<Emprestimo | null> => {
  return useFetch<Emprestimo>(`${BACKEND_URL}/emprestimo/`, {
    method: 'POST',
    body: venda
  })
    .then(resposta => {
      return Promise.resolve(resposta.data.value);
    })
    .catch(error => {
      console.log("error", error);
      return Promise.resolve(null);
    })
};


export const salvarVendaProdutos = (vendas: Array<EmprestimoLivroBody>): Promise<EmprestimoLivro | null> => {
  return useFetch<EmprestimoLivro>(`${BACKEND_URL}/emprestimo-livro/`, {
    method: 'POST',
    body: vendas
  })
    .then(resposta => {
      return Promise.resolve(resposta.data.value);
    })
    .catch(error => {
      console.log("error", error);
      return Promise.resolve(null);
    })
};



