Coin = Class{}

function Coin:init(params)
    self.x = params.x
    self.y = params.y
    self.player = params.player
    self.yellow = self.player == 1 and true or false
end

function Coin:update(dt)

end

function Coin:render()

    love.graphics.setColor(255, 255, 255, 255)
    
    if self.yellow then
        love.graphics.draw(gTextures['yellow_coin'], (self.x - 1) * TILEGAPX + 7, self.y)
    else
        love.graphics.draw(gTextures['red_coin'], (self.x - 1) * TILEGAPX + 4, self.y - 2)
    end
end

