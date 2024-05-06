## wget https://raw.githubusercontent.com/sksq96/utils/master/setup.sh
## bash setup.sh


# zsh
sudo apt install zsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
echo "exec zsh" >> ~/.bashrc

# zsh-syntax-highlighting
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git .zsh-syntax-highlighting
echo "source ${(q-)PWD}/.zsh-syntax-highlighting/zsh-syntax-highlighting.zsh" >> ${ZDOTDIR:-$HOME}/.zshrc
source ./.zsh-syntax-highlighting/zsh-syntax-highlighting.zsh

source ~/.zshrc

# pyenv
curl https://pyenv.run | bash


### COPY BELOW to ~/.zshrc
CONFIG="
export PYENV_ROOT=\"\$HOME/.pyenv\"
[[ -d \$PYENV_ROOT/bin ]] && export PATH=\"\$PYENV_ROOT/bin:\$PATH\"
eval \"\$(pyenv init -)\"
eval \"\$(pyenv virtualenv-init -)\"
"
echo "$CONFIG" >> ~/.zshrc
source ~/.zshrc

# file transfer
sudo apt install magic-wormhole
curl https://getcroc.schollz.com | bash

# tools
sudo apt install nano tmux htop
