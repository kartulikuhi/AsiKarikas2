--[[
    ScoreState Class
    Author: Colton Ogden
    cogden@cs50.harvard.edu

    A simple state used to display the player's score before they
    transition back into the play state. Transitioned to from the
    PlayState when they collide with a Pipe.
]]

ScoreState = Class{__includes = BaseState}
local gold_medal = love.graphics.newImage('goldmedal.png')
local silver_medal = love.graphics.newImage('silvermedal.png')
local bronze_medal = love.graphics.newImage('bronzemdeal.png')
local result = ''

--[[
    When we enter the score state, we expect to receive the score
    from the play state so we know what to render to the State.
]]
function ScoreState:enter(params)
    self.score = params.score
    scrolling = true
    wastitlescreen = true
end

function ScoreState:update(dt)
    -- go back to play if enter is pressed
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

function ScoreState:render()
    -- simply render the score to the middle of the screen
    if self.score < 5 then
        love.graphics.setFont(flappyFont)
        love.graphics.printf('Oof! You lost!', 0, 64, VIRTUAL_WIDTH, 'center')
    end
    love.graphics.setFont(mediumFont)
    love.graphics.printf('Score: ' .. tostring(self.score), 0, 100, VIRTUAL_WIDTH, 'center')
    if self.score >= 5 then
        if self.score >= 15 then
            love.graphics.draw(gold_medal, VIRTUAL_WIDTH/2 - gold_medal:getWidth()/2*0.2, 40, 0, 0.2, 0.2)
            result = 'gold medal!'
        elseif self.score >= 10 then
            love.graphics.draw(silver_medal, VIRTUAL_WIDTH/2 - silver_medal:getWidth()/2*0.2, 40, 0, 0.2, 0.2)
            result = 'silver medal!'
        elseif self.score >= 5 then
            love.graphics.draw(bronze_medal, VIRTUAL_WIDTH/2 - bronze_medal:getWidth()/2*0.2, 40, 0, 0.2, 0.2)
            result = 'bronze medal!'
        end
        love.graphics.setFont(mediumFont)
        love.graphics.printf('Congratulations! You got a ' .. result, 0, 20, VIRTUAL_WIDTH, 'center')
    end
    love.graphics.setFont(mediumFont)
    love.graphics.printf('Press Enter to Play Again!', 0, 200, VIRTUAL_WIDTH, 'center')
end