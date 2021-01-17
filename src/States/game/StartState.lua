StartState = Class{__includes = BaseState}

function StartState:init()
    self.colors = {
        [1] = {255, 255, 0, 255},
        [2] = {255, 0, 0, 255},
        [3] = {0, 0, 255, 255},
        [4] = {255, 255, 0, 255},
        [5] = {255, 0, 0, 255},
        [6] = {0, 0, 255, 255},
        [7] = {255, 255, 0, 255},
        [8] = {255, 0, 0, 255},
        [9] = {0, 0, 255, 255},
        [10] = {255, 255, 0, 255},
        [11] = {255, 0, 0, 255},
    }

    self.chars = {
        {'C', -260},
        {'O', -210},
        {'N', -160},
        {'N', -110},
        {'E', -60},
        {'C', -10},
        {'T', 40},
        {'F', 130},
        {'O', 180},
        {'U', 230},
        {'R', 280}
    }

    self.letterColorTimer = Timer.every(0.8, function()

        self.colors[0] = self.colors[3]
        for i = 11, 1, -1 do
            self.colors[i] = self.colors[i - 1]
        end
    end)
end

function StartState:update(dt)

    if love.keyboard.wasPressed('return') or love.keyboard.wasPressed('enter') then
        gStateMachine:change('play')
    end

    if love.keyboard.wasPressed('escape') then
        love.event.quit()
    end
end

function StartState:render()

    love.graphics.setFont(gFonts['large'])
    self:ColorLetters()

    love.graphics.setFont(gFonts['medium'])
    love.graphics.printf('Press ENTER to begin!', VIRTUAL_WIDTH / 5 - 150, VIRTUAL_HEIGHT / 2 + 50, VIRTUAL_WIDTH, 'center')


end

function StartState:ColorLetters()
    for i = 1, 11 do
        love.graphics.setColor(self.colors[i])
        love.graphics.printf(self.chars[i][1], self.chars[i][2], VIRTUAL_HEIGHT / 2 - 64, VIRTUAL_WIDTH, 'center')
    end
end