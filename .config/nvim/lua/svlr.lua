vim.opt.number = true
vim.opt.relativenumber = true
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
--vim.cmd("colorscheme kanagawa")

-- Отключить стрелки
keymap("", "<Up>", "<NOP>", opts)
keymap("", "<Down>", "<NOP>", opts)
keymap("", "<Left>", "<NOP>", opts)
keymap("", "<Right>", "<NOP>", opts)

-- Копировать в буфер обмена
vim.keymap.set("v", "<C-c>", '"+y', { noremap = true, silent = true })
-- Вставить из буфера обмена
vim.keymap.set("i", "<C-v>", '<C-r>+', { noremap = true, silent = true })
vim.keymap.set("n", "<C-v>", '"+p', { noremap = true, silent = true })


