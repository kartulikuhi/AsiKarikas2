GameOverState = Class{__includes = BaseState}

function GameOverState:enter(params)
    self.player = params.player
    self.board = params.board
    self.tie = false
    if self.player == 0 then
        self.tie = true
    else
        self.winner = self.player == 1 and 'Yellow' or 'Red'
    end
end

function GameOverState:update(dt)
    if love.keyboard.wasPressed('enter') or love.keyboard.wasPressed('return') then
        gStateMachine:change('start')
    end

    if love.keyboard.wasPressed('escape') then
        love.event.quit()
    end
end

function GameOverState:render()

    if self.tie then
        love.graphics.setColor(255, 0, 0, 255)
        love.graphics.setFont(gFonts['large'])
        love.graphics.printf("It's a draw!", VIRTUAL_WIDTH / 2 - 320, 20, VIRTUAL_WIDTH, 'center')

    else
        love.graphics.setFont(gFonts['large'])
        if self.player == 1 then
            love.graphics.setColor(255, 0, 0, 255)
        else
            love.graphics.setColor(255, 255, 0, 255)
        end

        love.graphics.printf('Congratulations!', VIRTUAL_WIDTH / 2 - 320, 20, VIRTUAL_WIDTH, 'center')

        love.graphics.setFont(gFonts['medium'])

        if self.player == 1 then
            love.graphics.setColor(255, 255, 0, 255)
        else
            love.graphics.setColor(255, 0, 0, 255)
        end

        love.graphics.printf(self.winner .. ' player won !', VIRTUAL_WIDTH / 2 - 300, 100, VIRTUAL_WIDTH, 'center')
    end
    
    love.graphics.setFont(gFonts['small'])
    love.graphics.setColor(0, 0, 255, 255)
    love.graphics.printf('Press ENTER to play again!', VIRTUAL_WIDTH / 2 - 300, 140, VIRTUAL_WIDTH, 'center')

    self.board:render()
end