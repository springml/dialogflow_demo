package com.sml.demo.banking.model;

/**
 * Created by kaarthikraaj on 23/10/17.
 */


public class Data
{
    private Inputs[] inputs;

    private Conversation conversation;

    private User user;

    public Inputs[] getInputs ()
    {
        return inputs;
    }

    public void setInputs (Inputs[] inputs)
    {
        this.inputs = inputs;
    }

    public Conversation getConversation ()
    {
        return conversation;
    }

    public void setConversation (Conversation conversation)
    {
        this.conversation = conversation;
    }

    public User getUser ()
    {
        return user;
    }

    public void setUser (User user)
    {
        this.user = user;
    }

    @Override
    public String toString()
    {
        return "ClassPojo [inputs = "+inputs+", conversation = "+conversation+", user = "+user+"]";
    }
}


