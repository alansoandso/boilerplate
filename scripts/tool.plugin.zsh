_tool() {
  local completions

  completions="$(tool --list)"

  reply=(${(ps:\n:)completions})
}

# Complete with _tool
# '--env ' then return choice of (integration production)
# '--' then return choice between (verbose collections movies)


compctl -K _tool \
        -x 'c[-1,--env]' -k '(integration production)' - \
           's[--]' -k '(env verbose collections movies)' \
        -- tool

