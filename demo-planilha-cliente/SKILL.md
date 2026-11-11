---
name: demo-planilha-cliente
description: Cria a demonstração de uma planilha vendida pela Zorvyn para o cliente — vídeo animado com sons e a marca do cliente, imagens de cada aba e, se pedido, gravação da tela da planilha real.
---

# Demo de planilha para cliente (Zorvyn)

Use quando o Patrik pedir para mostrar ao cliente como uma planilha funciona: "faz um vídeo mostrando a planilha", "manda as fotos de cada aba", "grava a tela da planilha".

Antes de começar, avise na primeira linha: `⚙️ Nível recomendado: high`.

## O que entregar

1. **Vídeo animado** (MP4 vertical 1080x1920, 40–50 s) com a identidade do cliente.
2. **Uma imagem por aba** (PNG 1080x1350, formato 4:5 para WhatsApp).
3. **Opcional — gravação da planilha real**, só se o Patrik pedir.

Diga sempre ao Patrik que o vídeo e as imagens são montados com os dados de exemplo da planilha, não prints do Google Planilhas.

## Antes de montar: coletar a marca do cliente

- Logo **sem fundo** em PNG (versão escura e versão branca). Se só houver print do Instagram, recorte a maior versão disponível, separe a logo do fundo por limiar de cor, vetorize com `potrace` (pacote `potracer`) e exporte SVG + PNG 2000 px nas cores da marca, branca e preta.
- Paleta: 1 cor principal, 1 escura, 1 clara de fundo.
- Dados de exemplo da planilha (produtos, movimentações, saldos, KPIs) lidos da própria planilha pelo conector do Google Sheets. Nunca invente números diferentes dos da planilha.

## Parte 1 — Vídeo animado

Arquivos em `templates/`. Copie para uma pasta de trabalho junto com as logos.

1. Fontes: `npm i @fontsource/montserrat @fontsource/playfair-display @fontsource/great-vibes` na pasta de trabalho (Google Fonts não carrega no container).
2. Edite `video.html`:
   - Troque as cores em `:root` pela paleta do cliente.
   - Troque `logo_cor.png` / `logo_branca.png` pelas logos do cliente. A logo pequena (`#corner`) fica no canto superior direito do início ao fim, exceto na abertura e no fechamento, onde a logo aparece grande.
   - Ajuste textos e números de cada cena para os dados reais.
3. Estrutura das cenas (cada `<section class="scene" data-s data-e>`):
   abertura → cada aba que o cliente preenche → estoque/saldo com cores → trava de segurança → painel com números subindo e barras → aba do celular → fechamento com "Desenvolvido por Zorvyn Soluções Digitais · zorvyn.com.br".
4. Animações: classes `a pop|up|left|fadein|grow|shake` com `data-t` (segundo em que começam). Contadores: `data-count="de,até" data-tt="t0,t1" data-fmt="brl|pct"`. Digitação: `data-type="texto" data-t0 data-cps`.
5. Sons: coloque `data-sfx="pop|tick|whoosh|ding|coin|error"` no elemento; a digitação e os contadores geram sons sozinhos. Trilha de fundo é gerada baixinha em `snd.py`.
6. Pré-visualize antes de gravar: `node preview.js 3.5 10 16 ...` e confira os quadros.
7. Grave: `node rec.js` (30 fps, gera `frames/` e `sfx.json`; ajuste a duração `N` se mudar o tempo total).
8. Som: `python3 snd.py` (ajuste `D` para a duração total).
9. Junte: `ffmpeg -framerate 30 -i frames/f%05d.jpg -i sfx.wav -c:v libx264 -preset veryfast -crf 20 -pix_fmt yuv420p -c:a aac -b:a 160k -shortest -movflags +faststart Cliente_Como_Funciona.mp4`.

## Parte 2 — Imagens de cada aba

`abas.js` fotografa cada `<div class="sec" id="sN">` de um `abas.html` (540x675 CSS, escala 2). Monte `abas.html` reaproveitando o `<style>` do `video.html`, com um bloco por aba: etiqueta "Aba X", título com uma palavra em itálico na cor da marca, uma linha explicando a aba e a tabela ou cartões com os dados de exemplo. Use `white-space:nowrap` nos valores em R$. Monte uma folha de contato e confira antes de enviar.

## Parte 3 — Gravação da planilha real (opcional)

1. Abra a planilha no navegador do app Claude no computador do Patrik (built-in browser). Se aparecer "Você precisa ter acesso", a conta logada no navegador não é a dona da planilha: peça ao Patrik para trocar a conta ou autorizar compartilhar com a conta logada. Não compartilhe sem autorização.
2. Ligue o gravador do Windows (Xbox Game Bar: Win+Alt+R) com computer use; ele grava a janela em foco (o app Claude).
3. Passe por cada aba, faça um cadastro e uma venda de teste e mostre o saldo e o painel mudando.
4. Pare a gravação (Win+Alt+R). O vídeo fica em `Vídeos\Capturas`.
5. Apague os lançamentos de teste da planilha.

Se o Game Bar não estiver disponível, sugira ao Patrik gravar pelo celular (Samsung: painel rápido › Gravador de tela) e passe um roteiro de toques por aba.

## Entrega

- Envie o MP4 e as imagens com SendUserFile e salve no Drive em `Projetos/<Cliente>`.
- Avise que não é possível ouvir o áudio daqui: o Patrik deve assistir uma vez antes de mandar.
