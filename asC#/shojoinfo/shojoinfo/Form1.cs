
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace shojoinfo
{
    public partial class Shojoinfo : Form
    {
        public void openurl()
        {
            
        }

        public Shojoinfo()
        {
            InitializeComponent();
            makecommonfightTabs();
        }
        public class level:TabPage
        {
            private void buttonEvent(object sender, EventArgs e)
            {
                System.Diagnostics.Process.Start("https://naver.com");
            }
            public level(string name)
            {
                TableLayoutPanel layout = new TableLayoutPanel();
                layout.Anchor = (((AnchorStyles.Top | AnchorStyles.Bottom)
            | AnchorStyles.Left)
            | AnchorStyles.Right);
                layout.ColumnCount = 3;
                layout.RowCount = 6;
                int high = 0;
                if (Convert.ToInt32(name) == 0)
                    high = 4;
                else
                    high = 6;
                for(int i=0;i<high;i++)
                {
                    for(int j=0;j<3;j++)
                    {
                        Button a = new Button();
                        string buttonname = "";
                        buttonname += name+'-'+(i+1).ToString();
                        switch(j)
                        {
                            case 1:
                                buttonname += 'E';
                                break;
                            case 2:
                                buttonname += 'N';
                                break;
                        }
                        a.Text = buttonname;
                        a.Size = new Size(80, 30);
                        a.Click += buttonEvent;
                        layout.Controls.Add(a);
                    }
                }
                Text = name;
                layout.Location = new Point(50, 40);
                Controls.Add(layout);
            }

        }
        /// <summary>
        /// 지역 탭
        /// </summary>
        private void makecommonfightTabs()
        {
            for (int i = 0; i < 12; i++)
            {
                string name = i.ToString();
                level tab = new level(name);
                commonfightTabControl.Controls.Add(tab);
            }
            Console.Write("make check");
        }
    }
}
