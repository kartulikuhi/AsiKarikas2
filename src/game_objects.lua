--[[
    GD50
    Legend of Zelda

    Author: Colton Ogden
    cogden@cs50.harvard.edu
]]

GAME_OBJECT_DEFS = {
    ['switch'] = {
        type = 'switch',
        texture = 'switches',
        frame = 2,
        width = 16,
        height = 16,
        solid = false,
        defaultState = 'unpressed',
        states = {
            ['unpressed'] = {
                frame = 2
            },
            ['pressed'] = {
                frame = 1
            }
        }
    },
    ['pot'] = {
        type = 'pot',
        texture = 'tiles',
        frame = 111,
        width = 8,
        height = 16,
        solid = true,
        defaultState = 'pot',
        states = {
            ['pot'] = {
                frame = 111
            }
        },
        pickedUp = false,
        thrown = false
    },
    ['heart'] = {
        type = 'heart',
        texture = 'hearts',
        frame = 5,
        width = 16,
        height = 16,
        solid = false,
        consumable = true,
        defaultState = 'heart',
        states = {
            ['heart'] = {
                frame = 5
            }
        },
        onConsume = function(player)
            if player.health <= 4 then
                player.health = player.health + 2
            else
                player.health = 6
            end
        end
    }
}