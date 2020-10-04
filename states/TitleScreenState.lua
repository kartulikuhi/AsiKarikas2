--[[
    TitleScreenState Class
    Author: Colton Ogden
    cogden@cs50.harvard.edu

    The TitleScreenState is the starting screen of the game, shown on startup. It should
    display "Press Enter" and also our highest score.
]]

TitleScreenState = Class{__includes = BaseState}

function TitleScreenState:enter()
    wastitlescreen = true
end
function TitleScreenState:update(dt)
    -- transition to countdown when enter/return are pressed
    if love.keyboard.wasPressed('enter') or love.keyboard.wasPressed('return') then
        gStateMachine:change('countdown', {
            score = 0,
            lastY = -PIPE_HEIGHT + math.random(80) + 20,
            bird = Bird(),
            pipePairs = {},
            timer = 0,
            counttime = 3
        })
    end
end

function TitleScreenState:render()
    -- simple UI code
    love.graphics.setFont(flappyFont)
    love.graphics.printf('Fifty Bird', 0, 64, VIRTUAL_WIDTH, 'center')

    love.graphics.setFont(mediumFont)
    love.graphics.printf('Press Enter to start', 0, 100, VIRTUAL_WIDTH, 'center')
    love.graphics.setFont(smallFont)
    love.graphics.printf("Press 'SPACEBAR' or click the left mouse button to jump.", 0, VIRTUAL_HEIGHT - 80, VIRTUAL_WIDTH, 'center')
    love.graphics.printf("Press 'p' to pause the game while playing.", 0, VIRTUAL_HEIGHT - 50, VIRTUAL_WIDTH, 'center')
end