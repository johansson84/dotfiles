# Output system info
# cowfortune
archey3 | lolcat

# Path to your oh-my-zsh installation.
export ZSH=/home/victor/.oh-my-zsh

# Set name of the theme to load.
# Look in ~/.oh-my-zsh/themes/
# ZSH_THEME="spaceship"
ZSH_THEME="pure"

# Uncomment the following line to display red dots whilst waiting for completion.
COMPLETION_WAITING_DOTS="true"

# Uncomment the following line if you want to change the command execution time
# stamp shown in the history command output.
# The optional three formats: "mm/dd/yyyy"|"dd.mm.yyyy"|"yyyy-mm-dd"
HIST_STAMPS="yyyy-mm-dd"

# Which plugins would you like to load? (plugins can be found in ~/.oh-my-zsh/plugins/*)
# Custom plugins may be added to ~/.oh-my-zsh/custom/plugins/
# Example format: plugins=(rails git textmate ruby lighthouse)
# Add wisely, as too many plugins slow down shell startup.
plugins=(gitfast archlinux z zsh-syntax-highlighting zsh-autosuggestions)

# User configuration

# export PATH="/usr/bin:/bin:/usr/sbin:/sbin:$PATH"
# export MANPATH="/usr/local/man:$MANPATH"

source $ZSH/oh-my-zsh.sh

# You may need to manually set your language environment
# export LANG=en_US.UTF-8

# Preferred editor for local and remote sessions
if [[ -n $SSH_CONNECTION ]]; then
  export EDITOR='vim'
else
  export EDITOR='vim'
fi

# Compilation flags
# export ARCHFLAGS="-arch x86_64"

# ssh
# export SSH_KEY_PATH="~/.ssh/dsa_id"

# Set personal aliases, overriding those provided by oh-my-zsh libs,
# plugins, and themes. Aliases can be placed here, though oh-my-zsh
# users are encouraged to define aliases within the ZSH_CUSTOM folder.
# For a full list of active aliases, run `alias`.
#
# Example aliases
alias zshconfig="vim ~/.zshrc"
alias ohmyzsh="vim ~/.oh-my-zsh"
alias xrandr3="xrandr --output eDP1 --mode 1920x1080 && xrandr --output DP3-1 --mode 1920x1080 --right-of eDP1 && xrandr --output DP3-2 --mode 1920x1080 --right-of DP3-1 --rotate left"
alias tid="php ~/Documents/Fortnox/Git/phptid/tid.php \"&@\""
alias googler="/home/victor/Documents/Slask/googler/googler"
alias spotify-cli="~/Documents/Slask/pms/mps"
alias rss="newsbeuter"
alias wod="python ~/bin/wod.py"
alias food="python ~/bin/food.py"

# Alias for fixing network?
# nmcli networking off
# nmcli networking on
# nmcli general status

export PATH=$PATH:/home/victor/bin
export GOPATH=$HOME/go
export PATH=$PATH:$GOPATH/bin

XDG_CONFIG_HOME="$HOME/.config"
export XDG_CONFIG_HOME

