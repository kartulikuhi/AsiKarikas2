Board = Class{}

function Board:init()
    self.tileMap = self:generateBoard()
    self.coins = {}
end

function Board:update(dt)

end

function Board:render()

    for k, coin in pairs(self.coins) do
        coin:render()
    end

    love.graphics.setColor(255, 255, 255, 255)
    love.graphics.draw(gTextures['board'], 0, 160, 0)

end

function Board:generateBoard()
    local tileMap = {}
    for x = 1, 7 do
        table.insert(tileMap, {})
        for y = 1, 6 do
            table.insert(tileMap[x], false)
        end
    end

    return tileMap
end

function Board:calculateWins(player)
    local counter = 0
    local win = false
    --vertical
    for x = 1, 7 do
        counter = 0
        for y = 1, 6 do

            if self.tileMap[x][y] == player then
                counter = counter + 1
            else
                counter = 0
            end

            if counter >= 4 then
                win = true
                break
            end

        end
        
        if win then
            break
        end

    end
    --horizontal
    for y = 1, 6 do
        counter = 0
        for x = 1, 7 do

            if self.tileMap[x][y] == player then
                counter = counter + 1
            else
                counter = 0
            end

            if counter >= 4 then
                win = true
                break
            end

        end

        if win then
            break
        end

    end

    --diagonal (left to right)

    for y = 6, 4, -1 do
        for x = 1, 4 do
            counter = 0
            
            for i = 0, 3 do

                if self.tileMap[x + i][y - i] == player then
                    counter = counter + 1
                else
                    counter = 0
                end

                if counter >= 4 then
                    win = true
                    break
                end
            end

            if win then
                break
            end

        end

        if win then
            break
        end

    end

    --diagonal (right to left)

    for y = 6, 4, -1 do
        for x = 7, 4, -1 do
            counter = 0

            for i = 0, 3 do

                if self.tileMap[x - i][y - i] == player then
                    counter = counter + 1
                else
                    counter = 0
                end

                if counter >= 4 then
                    win = true
                    break
                end
            end

            if win then
                break
            end
            
        end

        if win then
            break
        end
    end

    return win

end