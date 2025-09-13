vim.opt.number = true
vim.opt.syntax = "on"
vim.opt.expandtab = true
vim.opt.tabstop = 4
vim.opt.shiftwidth = 4
vim.opt.smartindent = true
vim.opt.mouse = "a"
vim.opt.clipboard = "unnamedplus"
vim.opt.hlsearch = true
vim.opt.incsearch = true
vim.opt.ignorecase = true
vim.opt.smartcase = true
vim.opt.scrolloff = 5
vim.opt.cursorline = true
vim.opt.showmatch = true
vim.opt.colorcolumn = "79"
vim.g.mapleader = " "
vim.opt.termguicolors = true

local keymap = vim.keymap.set
local opts = { noremap = true, silent = true }
-- Отключил стрелки
keymap("", "<Up>", "<NOP>", opts)
keymap("", "<Down>", "<NOP>", opts)
keymap("", "<Left>", "<NOP>", opts)
keymap("", "<Right>", "<NOP>", opts)
-- Вставка и копирование
keymap("v", "<C-c>", '"+y', opts)
keymap("i", "<C-v>", '<C-r>+', opts)
keymap("n", "<C-v>", '"+p', opts)
-- COC
-- Перейти к определению
keymap("n", "gd", "<Plug>(coc-definition)", opts)
-- Показать документацию
keymap("n", "K", ":call CocActionAsync('doHover')<CR>", opts)
-- Переименовать символ
keymap("n", "<leader>rn", "<Plug>(coc-rename)", opts)
-- Показать все ссылки на символ
keymap("n", "gr", "<Plug>(coc-references)", opts)
-- Автокомплит / подсказки
keymap("i", "<C-Space>", "coc#refresh()", { expr = true, silent = true })

-- Быстрый выбор из подсказок автокомплита
keymap("i", "<CR>", [[coc#pum#visible() ? coc#pum#confirm() : "\<CR>"]], { expr = true, silent = true })
keymap("i", "<Tab>", [[coc#pum#visible() ? coc#pum#next(1) : "\<Tab>"]], { expr = true, silent = true })
keymap("i", "<S-Tab>", [[coc#pum#visible() ? coc#pum#prev(1) : "\<S-Tab>"]], { expr = true, silent = true })
