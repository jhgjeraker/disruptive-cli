# Bash completion for disruptive-cli.

_dt_complete()
{
    local cur prev
    COMPREPLY=()
    cur=${COMP_WORDS[COMP_CWORD]}
    prev=${COMP_WORDS[COMP_CWORD-1]}

    if [ $COMP_CWORD -eq 1 ]; then
        COMPREPLY=( $(compgen -W "device dataconnector project organization serviceaccount role event emulator claim config" -- $cur) )
    elif [ $COMP_CWORD -eq 2 ]; then
        case "${COMP_WORDS[COMP_CWORD-1]}" in
            "device")
                COMPREPLY=( $(compgen -W "get list transfer label" -- $cur) )
                ;;
            "dataconnector")
                COMPREPLY=( $(compgen -W "get list create update delete sync metrics" -- $cur) )
                ;;
            "project")
                COMPREPLY=( $(compgen -W "get list create update delete permissions member" -- $cur) )
                ;;
            "organization")
                COMPREPLY=( $(compgen -W "get list permissions member" -- $cur) )
                ;;
            "serviceaccount")
                COMPREPLY=( $(compgen -W "get list create update delete key" -- $cur) )
                ;;
            "role")
                COMPREPLY=( $(compgen -W "get list" -- $cur) )
                ;;
            "event")
                COMPREPLY=( $(compgen -W "list stream" -- $cur) )
                ;;
            "emulator")
                COMPREPLY=( $(compgen -W "create delete publish" -- $cur) )
                ;;
            "claim")
                COMPREPLY=( $(compgen -W "claim info" -- $cur) )
                ;;
            "config")
                COMPREPLY=( $(compgen -W "default padding" -- $cur) )
                ;;
            *)
                ;;
        esac
    elif [ $COMP_CWORD -eq 3 ]; then
        case "${COMP_WORDS[COMP_CWORD-2]}" in
            "device")
                case "${COMP_WORDS[COMP_CWORD-1]}" in
                    "label")
                        COMPREPLY=( $(compgen -W "set remove" -- $cur) )
                        ;;
                esac
                ;;
            "dataconnector")
                case "${COMP_WORDS[COMP_CWORD-1]}" in
                    "create")
                        COMPREPLY=( $(compgen -W "http-push" -- $cur) )
                        ;;
                    "update")
                        COMPREPLY=( $(compgen -W "http-push" -- $cur) )
                        ;;
                esac
                ;;
            "project")
                case "${COMP_WORDS[COMP_CWORD-1]}" in
                    "member")
                        COMPREPLY=( $(compgen -W "add remove get update list invite-url" -- $cur) )
                        ;;
                esac
                ;;
            "organization")
                case "${COMP_WORDS[COMP_CWORD-1]}" in
                    "member")
                        COMPREPLY=( $(compgen -W "add remove get list invite-url" -- $cur) )
                        ;;
                esac
                ;;
            "serviceaccount")
                case "${COMP_WORDS[COMP_CWORD-1]}" in
                    "key")
                        COMPREPLY=( $(compgen -W "get list create delete" -- $cur) )
                        ;;
                esac
                ;;
            "emulator")
                case "${COMP_WORDS[COMP_CWORD-1]}" in
                    "publish")
                        COMPREPLY=( $(compgen -W "touch temperature object-present humidity object-present-count touch-count water-present network-status battery-status connection-status ethernet-status cellular-status co2 pressure motion desk-occupancy" -- $cur) )
                        ;;
                esac
                ;;
            *)
                ;;
        esac
    fi
}


complete -F _dt_complete dt
