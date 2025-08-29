-- Загрузка плагинов
require("lazy").setup({
  -- Файловый менеджер
  { "preservim/nerdtree" },

  -- Парные скобки (аналог delimitmate)
  { "windwp/nvim-autopairs", config = true },

  -- Подсветка синтаксиса с деревом разбора
  {
    "nvim-treesitter/nvim-treesitter",
    build = ":TSUpdate",
    config = function()
      require("nvim-treesitter.configs").setup {
        ensure_installed = { "c", "lua", "rust", "python" }, -- нужные языки
        highlight = {
          enable = true,
          additional_vim_regex_highlighting = false,
        },
        indent = {
          enable = true,
        },
      }
    end,
  },

  -- Статусбар
  { "nvim-lualine/lualine.nvim" },

  -- Отображение соответствующих скобок
  { "andymass/vim-matchup" },

  {
     "rebelot/kanagawa.nvim",
     lazy = false,  -- загружаем сразу, чтобы тема применялась
     config = function()
       vim.cmd("colorscheme kanagawa-dragon")
     end,
  },

  {
          "powerman/vim-plugin-ruscmd",
          lazy = false
  },
})

