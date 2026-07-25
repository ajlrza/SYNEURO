package main

import (
     "fmt"
     "log"
     "github.com/gofiber/fiber/v3"
     "net/url"
     //"net/http"
)

func main() {
     
     app := fiber.New()

     //networkClient := &http.Client{}

     app.Get("/", func(c fiber.Ctx) error {
        return c.SendString("Go Lang TEST 👋!")
     })

     app.Post("/interact", func(c fiber.Ctx) error {
        if !c.HasBody() {
            return c.SendStatus(fiber.StatusBadRequest)
        }

        body := c.Body()
        req_url := c.FullURL()

    })

     app.Post("/cache-memory", func(c fiber.Ctx) error {

        if !c.HasBody() {
            return c.SendStatus(fiber.StatusBadRequest)
        }
     
        body := c.Body()
        u, err := url.Parse(c.FullURL())

        if err != nil {
            return c.SendStatus(fiber.StatusBadRequest) 
        }

        userId := u.Query().Get("userid") 

        if userId == "" {
            fmt.Println("User not found in the request... attemping to ask the client.")
            ask_unknown_user := map[string]any{
                "Unknown": true,
            }

            return c.JSON(ask_unknown_user)
        }

        memory_cache = body

    })

     log.Fatal(app.Listen(":3000"))
     fmt.Println("Server sarted at https://localhost/3000")
}