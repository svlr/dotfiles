-- bootstrap lazy.nvim
local lazypath = vim.fn.stdpath("data") .. "/lazy/lazy.nvim"
if not vim.loop.fs_stat(lazypath) then
  vim.fn.system({
    "git", "clone", "--filter=blob:none",
    "https://github.com/folke/lazy.nvim.git",
    lazypath
  })
end
vim.opt.rtp:prepend(lazypath)

-- load plugins
require("lazy").setup({
  -- coc.nvim для автокомплита и LSP
  {
    "neoclide/coc.nvim",
    branch = "release",
    build = "npm ci",
  },

  -- Дополнительно:
   { "preservim/nerdtree" },
  { "windwp/nvim-autopairs", config = true },
  {
    "nvim-treesitter/nvim-treesitter",
    build = ":TSUpdate",
    config = function()
      require("nvim-treesitter.configs").setup({
        ensure_installed = { "lua", "c", "rust", "python" },
        highlight = { enable = true },
        indent = { enable = true },
      })
    end,
  },
  { "nvim-lualine/lualine.nvim" },
  { "andymass/vim-matchup" },
  {
    "rebelot/kanagawa.nvim",
    lazy = false,
    config = function()
      vim.cmd("colorscheme kanagawa-dragon")
    end,
  },
})
