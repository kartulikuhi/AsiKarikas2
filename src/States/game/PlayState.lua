PlayState = Class{__includes = BaseState}

function PlayState:init()

    self.board = Board()
    self.selectedX = 1
    self.player = 1
    self.activeCoin = Coin({x = 1, y = 50, player = self.player})
    self.canInput = true
    self.turnCount = 1

end

function PlayState:update(dt)

    if love.keyboard.wasPressed('escape') then
        love.event.quit()
    end

    if self.canInput then
        if love.keyboard.wasPressed('d') or love.keyboard.wasPressed('right') then
            self.activeCoin.x = self.activeCoin.x == 7 and 1 or self.activeCoin.x + 1
            gSounds['selection']:play()
        end

        if love.keyboard.wasPressed('a') or love.keyboard.wasPressed('left') then
            self.activeCoin.x = self.activeCoin.x == 1 and 7 or self.activeCoin.x - 1
            gSounds['selection']:play()
        end


        if love.keyboard.wasPressed('enter') or love.keyboard.wasPressed('return') then

            local error_beep = true

            for table_y = 6, 1, -1 do
                if self.board.tileMap[self.activeCoin.x][table_y] == false then

                    self.board.tileMap[self.activeCoin.x][table_y] = self.activeCoin.player
                    table.insert(self.board.coins, self.activeCoin)

                    error_beep = false
                    self.canInput = false
                    self.turnCount = self.turnCount + 1

                    Timer.tween(0.1 * table_y, {
                        [self.activeCoin] = {y = table_y * TILEGAPY + 80}
                    }):finish(function()

                        if self.board:calculateWins(self.player) then
                            gSounds['win']:play()
                            Timer.after(0.5, function()
                                gStateMachine:change('game-over', {player = self.player, board = self.board})
                            end)
                        else

                            if self.turnCount > 42 then
                                Timer.after(0.5, function()
                                    gSounds['win']:play()
                                    gStateMachine:change('game-over', {player = 0, board = self.board})
                                end)
                            else
                            
                                self.player = self.player == 1 and 2 or 1

                                local previousX = self.activeCoin.x
                                self.activeCoin = Coin({x = previousX, y = 50, player = self.player})

                                gSounds['coin']:play()
                                self.canInput = true
                            end
                        end

                    end)

                    break
                end
            end

            if error_beep then
                gSounds['error']:play()
            end

        end
    end

    self.board:update(dt)


end

function PlayState:render()
    self.activeCoin:render()
    self.board:render()
end