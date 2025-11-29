def define_env(env):
    @env.macro
    def icon(name):
        return f'<span class="material-symbols-outlined material-icon">{name}</span>'
