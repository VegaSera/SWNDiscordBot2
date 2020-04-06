
async def toggle_group(role_title, ctx):
    """Toggles the user's roles. For example, adds a role if they do not have it already, or removes it if they do.
    We allow the message handling to be done by the function calling this function, for more customizability.
    Function has four potential return results.
    'whisper' - The user is whispering the bot. They dumb.
    'role not found' - Did not find this particular role on the server in question.
    'removed' - Role was removed from the user
    'added' - Role was added to the user."""
    if ctx.guild is None:
        return 'whisper'
    server_roles = ctx.guild.roles
    #print("Server roles", server_roles)
    user_roles = ctx.author.roles
    #print("Author roles", user_roles)

    role_id = ""

    #Finding the role on the server. If it doesn't exist, we'll let the user know.
    found_role = False
    role_id_index = ''
    for i in server_roles:
        #print(i.name.lower())
        if i.name.lower() == role_title.lower(): #.lower is for consistency
            role_id = i
            found_role = True
            try:
                role_id_index = user_roles.index(i)
            except:
                pass

    if not found_role:
        return "role not found"
    else:
        if role_id in user_roles:
            # User has this role, need to remove it.
            user_roles.pop(role_id_index)
            await ctx.author.edit(roles=user_roles, reason="Automated role removal requested by user")
            return "removed"
        else:
            # User does not have this role
            user_roles.append(role_id)
            await ctx.author.edit(roles=user_roles, reason="Automated role add requested by user")
            return "added"







