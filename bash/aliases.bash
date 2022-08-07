alias jjgit_changed_files='git diff --name-only main --diff-filter=d'
alias jjgit_changed_pyfiles='git diff --name-only main --diff-filter=d "*.py"'
alias jjgit_code_changed_files='code `jjgit_changed_files`'
alias jjgit_changed_tests='jjgit_changed_pyfiles | grep test'
alias jjgit_pylint='pylint `jjgit_changed_pyfiles`'
alias jjgit_isort='isort `jjgit_changed_pyfiles`'
alias jjgit_mypy='mypy `jjgit_changed_pyfiles`'
alias jjgit_black='black `jjgit_changed_pyfiles`'
alias jjgit_quality='echo isort; jjgit_isort; echo black; jjgit_black; echo pylint; jjgit_pylint; echo mypy; jjgit_mypy'
alias jjbashrc='source ~/.bashrc'
alias jjgit_log='git log --first-parent'
alias jjgit_log_fancy='git log --graph --abbrev-commit --decorate --all --author=gettodaze \
    --format=format:"%C(bold blue)%h%C(reset) - %C(bold cyan)%aD%C(dim white) \
    - %an%C(reset) %C(bold green)(%ar)%C(reset)%C(bold yellow)%d%C(reset)%n %C(white)%s%C(reset)"'
alias jjgit_prune='git fetch --prune --all'
alias test_mic='pactl load-module module-loopback latency_msec=1000'
alias test_mic_stop='pactl unload-module module-loopback'
alias tmux_kill_others='tmux kill-session -a'
alias reset_audio='pulseaudio -k && sudo alsa force-reload'
alias jjgit_revert1='git revert HEAD~1..HEAD --no-commit'
alias contents_by_size='du -hd 1| sort -h'
alias jjtree="tree -I '_*|*.pyc'"
alias jjtom_git_prune='git branch --merged| egrep -v "(^\*|main|master|main)" | xargs git branch -d'
alias jjcurrent_dir='basename `pwd`'
alias jjzip_current_dir='zip -r `jjcurrent_dir` .'
alias jjgrep_pyfiles_nameonly='grep -irl --include \*.py'
function lbc {
    libreoffice --calc $1 2>/dev/null 1>&2 &
}

function newbranch {
    while true; do
        git status
        read -p "Do you wish to create $1? [y/n] " yn
        case $yn in
            [Yy]* ) break;;
            [Nn]* ) return 1;;
            * ) echo "Please answer yes or no.";;
        esac
    done
    # echo "created $1"
    git branch $1
    git checkout $1
    git push --set-upstream origin $1
}

function jjfile_header {
    head -n1 $1 | tr '\t' '\n'
}

function jjgit_merge_main {
    git checkout main
    git pull
    git checkout -
    git merge main
}

parse_git_branch() {
     git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/ (\1)/'
}

function jj_dos2unix {
    mv $1 .dos_$1
    tr -d '\15\32' < .dos_$1 > $1
}

# export PS1="\[\033[32m\](${VIRTUAL_ENV##*/}) \[\033[34m\]\W\[\033[37m\]\$ "

# export PROMPT_COMMAND="echo -n \[\$(date +%H:%M)\]\ "

# run with 'source ~/.bashrc'
