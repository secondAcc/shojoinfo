
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

        public Shojoinfo()
        {
            InitializeComponent();
            makecommonfightTabs();
        }

        /// <summary>
        /// 지역 탭
        /// </summary>
        private void makecommonfightTabs()
        {

            for (int i = 0; i < 12; i++)
            {
                string name = i.ToString();
                TabPage tab = new TabPage(i.ToString());
                //tab.Controls.Add(hardtab);
                commonfightTabControl.Controls.Add(tab);
            }
            Console.Write("make check");
        }
    }
}
