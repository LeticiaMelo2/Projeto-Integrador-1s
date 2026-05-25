// Função pra abrir o modal com os dados
function abrirDetalhes(id, titulo, status, prioridade, usuario, descricao) {
    document.getElementById('modal-id').textContent = id;
    document.getElementById('modal-titulo').textContent = titulo;
    document.getElementById('modal-status').textContent = status;
    document.getElementById('modal-prioridade').textContent = prioridade;
    document.getElementById('modal-usuario').textContent = usuario;
    document.getElementById('modal-descricao').textContent = descricao;
    document.getElementById('modal-detalhes').style.display = 'block';
}

// Fecha o modal quando clicar no X
document.addEventListener('DOMContentLoaded', function() {
    // Fecha pelo X
    const closeBtn = document.querySelector('.modal-close');
    if (closeBtn) {
        closeBtn.onclick = function() {
            document.getElementById('modal-detalhes').style.display = 'none';
        }
    }

    // Fecha clicando fora do modal
    window.onclick = function(event) {
        const modal = document.getElementById('modal-detalhes');
        if (event.target == modal) {
            modal.style.display = 'none';
        }
    }
});